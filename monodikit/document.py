import glob
import json
from dataclasses import dataclass, field
from typing import List
from xml.sax.saxutils import escape
import functools




@dataclass()
class Accidental:
    uuid: str
    base: str
    liquescent: str
    noteType: str
    octave: int
    focus: bool

    @property
    def mei(self):
        if self.noteType == "Flat":
            accid = "f"
        elif self.noteType == "Natural":
            accid = "n"
        else:
            accid = "?"

        return f'<accid ploc="{self.base}" poct="{self.oct}" accid="{accid}"'


@dataclass
class NeumeComponent:
    uuid: str
    base: str
    liquescent: bool
    noteType: str
    octave: int
    focus: bool
    ncIndex: int
    note_to_num = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}

    def calculate_number(self):
        return (self.octave * 7) + (self.note_to_num[self.base])

    def __lt__(self, other):
        return self.calculate_number() < other.calculate_number()

    def __gt__(self, other):
        return self.calculate_number() > other.calculate_number()

    def __le__(self, other):
        return self.calculate_number() <= other.calculate_number()

    def __ge__(self, other):
        return self.calculate_number() >= other.calculate_number()

    def __eq__(self, other):
        return self.calculate_number() == other.calculate_number() and self.liquescent == other.liquescent

    @property
    def pitch(self):
        return self.base + str(self.octave)

    @property
    def mei(self):
        if self.ncIndex == 0:
            con = ""
        else:
            con = ' con="g"'

        if self.liquescent:
            return f'<nc pname="{self.base.lower()}" oct="{self.octave}"{con}><liquescent/></nc>'
        elif self.noteType != "Normal":
            return f'<nc pname="{self.base.lower()}" oct="{self.octave}"{con}><{self.noteType}/></nc>'
        else:
            return f'<nc pname="{self.base.lower()}" oct="{self.octave}"{con}/>'

    @property
    def json(self):
        return {"type": "note", "pitch": f"{self.base}{self.octave}"}

    def __str__(self):
        return f"<NeumeComponent base={self.base}, oct={self.octave}>"

    def __repr__(self):
        return f"<NeumeComponent base={self.base}, oct={self.octave}>"



@dataclass
class EmptyNeumeComponent(NeumeComponent):
    @property
    def pitch(self):
        return "Empty"

    @property
    def mei(self):
        return ""


class Neume:
    """
    A class representing a neume loosely following the MEI specification.
    """

    def __init__(self, spaced_element):  #: Takes a dictionary representing the spaced element of the neume.
        self.neume_content = self.get_neume_content(spaced_element)  #: A list of `NeumeComponent` objects.
        self.neume_components = [element for element in self.neume_content if type(element) == NeumeComponent]
        self.accidentals = [element for element in self.neume_content if type(element) == Accidental]

    def parse_neume_content(self, element, index):
        try:
            if element["noteType"] == "Normal":
                neume = NeumeComponent(**element, ncIndex=index)
                low_peak = NeumeComponent(uuid="", base="G", liquescent=False,noteType="Normal", octave=3, focus=False, ncIndex=0)
                comment_note = NeumeComponent(uuid="", base="A", liquescent=True, noteType="Normal", octave=5, focus=False, ncIndex=0)
                if neume < low_peak or neume == comment_note:
                    return EmptyNeumeComponent(**element, ncIndex=index)
                else:
                    return neume
            elif element["noteType"] == "Flat" or element.noteType == "Natural":
                return Accidental(**element)
        except AttributeError:
            return None

    def get_neume_content(self, spaced_element):
        return [self.parse_neume_content(connected_neume_component, index=index)
                for neume_component in spaced_element["nonSpaced"]
                for index, connected_neume_component in enumerate(neume_component["grouped"])]

    @property
    def mei(self):
        neume_components = "".join([nc.mei for nc in self.neume_components])
        if len(self.accidentals):
            accidentals = "".join([accid.mei for accid in self.accidentals])
        else:
            accidentals = ""
        return f"{accidentals}<neume>{neume_components}</neume>"

    @property
    def json(self):
        return {"type": "neume", "elements": [neume_components.json for neume_components in self.neume_components]}


@dataclass
class Syllable:
    uuid: str
    kind: str
    text: str = ""
    syllableType: str = ""
    notes: dict = field(default_factory=dict)  # Notes good terminology? includes groups etc.
    endsWord: bool = False
    focus: bool = False
    hasNotes: bool = None
    neumes: list = field(init=False)  # How to name elements / notes? notes is now input, elements the

    # processed Notes instance
    def __post_init__(self):
        self.neumes = self.get_neumes(self.notes)

    def get_neumes(self, notes):
        if "spaced" not in notes:
            return []
        return [Neume(neume) for neume in notes["spaced"]]

    @property
    def mei(self):
        neumes = "".join([neume.mei for neume in self.neumes])
        return f"<syllable><syl>{escape(self.text)}</syl>{neumes}</syllable>"

    @property
    def json(self):
        return {"type": "syllable", "lyric": self.text, "elements": [neume.json for neume in self.neumes]}

@dataclass
class EditorialLine:
    pass

@dataclass
class Division:
    """
    A class representing a division of a medieval chant document.
    """
    data: list  #: A list of data elements for the division.
    children: list  #: A list of child elements for the division.

    # syllables : list = field(init=False)

    def __post_init__(self):
        children_wo_paratext = self.filter_paratexts(self.children)
        if "ZeileContainer" not in [values for child in children_wo_paratext for values in child.values()]:
            self.interdivision = True
            self.elements = [Division(d["data"], d["children"]) for d in children_wo_paratext]
            self.syllables: list = self.get_flat_syllables()
        else:
            self.interdivision = False
            self.syllables: list = self.get_syllables()  #: A list of `Syllable` objects representing the syllables in the division.

            #print("syllables", self.syllables)

        self.signature: str = self.get_signature()  #: The signature of the division, if present.
        self.status: str = self.get_status()  #: The status of the division, if present.

    def get_signature(self):
        division_metadata = {d["name"]: d["data"] for d in self.data}
        if "Signatur" in division_metadata.keys():
            return division_metadata["Signatur"]
        else:
            return None

    def get_status(self):
        dd = {d["name"]: d["data"] for d in self.data}
        if "Status" in dd.keys():
            return dd["Status"]
        else:
            return None

    def filter_paratexts(self, children):
        return [child for child in children if child["kind"] != "ParatextContainer"]


    def get_syllables(self):
        return [Syllable(**d) for child in self.filter_paratexts(self.children)  # ! How to model paratexts?
                for d in child["children"]
                ]

    def get_flat_syllables(self):
        if len(self.elements):
            if self.elements[0].interdivision:
                return [syllable for division in self.elements for syllable in division.get_flat_syllables()]
            else:
                return [syllable for division in self.elements for syllable in division.syllables]
        else:
            return []


    @property
    def flat_neumes(self):
        return [neume
                for syllable in self.syllables
                for neume in syllable.neumes]

    @property
    def flat_neume_components(self):
        return [note_component
                for syllable in self.syllables
                for neume in syllable.neumes
                for note_component in neume.neume_components]
        # if c["kind"] == "Syllable"

    @property
    def mei(self):
        if len(self.syllables) == 0:
            return ""
        syllables = "".join([syllable.mei for syllable in self.syllables])
        return f"<section><staff><layer>{syllables}</layer></staff></section>"

    @property
    def json(self):
        return {"type": "section", "elements": [syllable.json for syllable in self.syllables]}

    # def get_linechange(self):
    #     return [ Syllable(c) for child in self.children for d in child["children"] for c in d["children"] ]



class Chant:
    """
    A class representing a document or unit of medieval chant.

    A document is represented by its metadata and data,
    which are loaded from JSON files located in a directory specified
    by the entry parameter.
    """

    def __init__(self, entry_path):
        self.meta = self.get_meta(entry_path)
        data = self.get_data(entry_path)
        if data:
            self.data = data
        else:
            raise Exception("Could not load data", self.meta.id)
        self.type = self.meta.genre  #: The type of the document, taken from the gattung1 attribute of its metadata.

    @staticmethod
    def get_meta(entry_path):
        if glob.glob(entry_path + "/meta.json"):
            with open(entry_path + "/meta.json") as f:
                metadata = json.load(f)
                meta = Meta(**metadata)
            return meta
        else:
            return

    @staticmethod
    def get_data(entry):
        if glob.glob(entry + "/data.json"):
            with open(entry + "/data.json") as f:
                data = Data(**json.load(f))
            return data
        else:
            return None

    @property
    def flat_syllables(self):
        return [syllable
                for division in self.data.elements
                for syllable in division.syllables]

    @property
    def flat_neumes(self):
        return [neume
                for division in self.data.elements
                for neume in division.flat_neumes]
    @property
    def flat_neume_components(self):
        try:
            return [neume_component
                    for division in self.data.elements
                    for neume_component in division.flat_neume_components]
        except:
            print("Data.Elements is None at: ", self.meta.dokumenten_id)
            return []

    @property
    def flat_neume_components_by_division(self):
        return [[neume_component
                for neume_component in division.flat_neume_components]
                for division in self.data.elements]



    @property
    def mei(self):
        try:
            return f'<?xml version="1.0" encoding="UTF-8"?>' \
                   '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" ' \
                   'type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>' \
                   '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" ' \
                   'type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>' \
                   '<mei xmlns="http://www.music-encoding.org/ns/mei"><meiHead><fileDesc><titleStmt>' \
                   '<title></title></titleStmt><pubStmt></pubStmt></fileDesc></meiHead>' \
                   f'{self.data.mei}' \
                   '</mei>'
        except:
            print("Could not get MEI for: ", self.meta.dokumenten_id)
            return ""

    @property
    def json(self):
        return self.data.json



class Meta:

    def __init__(self, id, quelle_id, dokumenten_id, gattung1, gattung2, festtag, feier, textinitium,
               bibliographischerverweis, druckausgabe, zeilenstart, foliostart, kommentar, editionsstatus,
               additionalData):
        self.uuid = id,
        self.source_id = quelle_id
        self.document_id = dokumenten_id
        self.genre = gattung1
        self.subgenre = gattung2
        self.feast_day = festtag
        self.feast_time = feier
        self.initial_text = textinitium

        self.initial_folio = foliostart
        self.initial_line = zeilenstart
        self.ending_folio = additionalData.get("Endseite", "")
        self.ending_line = additionalData.get("Endzeile", "")

        self.bibliographical_reference = bibliographischerverweis
        self.cm_volume = druckausgabe

        self.editorial_comment = kommentar
        self.melody_number = additionalData.get("Melodiennummer_Katalog", "")
        self.melodyname_standardized = additionalData.get("Melodie_Standard", "")
        self.melodyname_diplomatic = additionalData.get("Melodie_Quelle", "")
        self.editor = additionalData.get("Editor", "")
        self.related_chant = additionalData.get("Bezugsgesang", "")
        self.liturgical_play_id = additionalData.get("Referenz_auf_Spiel", "")
        self.completeness = additionalData.get("Zusatz_zu_Textinitium", "")
        self.layer_of_addendum = additionalData.get("Nachtragsschicht", "")
        self.condition_of_transmission = additionalData.get("\u00dcberlieferungszustand", "")
        self.iiif_urls = additionalData.get("iiif", "")



@dataclass
class Data:
    """
    A class representing data of a medieval chant document.
    """
    comments: list  # TODO: list of dicts
    uuid: str
    kind: str
    children: list  # = field(init=False) #: The Input Data that is parsed by the model
    documentType: str  #: The DocumentType attribute specifies the number of hierarchical levels
                        # of Divisions the Document has
    elements: List[Division] = field(init=[])  #: The Division elements that are contained by the Document
    signatures: list = field(init=[])  #: A list of signatures for the elements of the document
    version: str = ""  #: to catch 'version' attribute in *some* data files


    def __post_init__(self):
        try:
            self.elements = [Division(d["data"], d["children"]) for d in self.children]
            self.signatures: List[str] = [e.signature for e in self.elements]
        except:
            print("Element parsing did not work with doc: ", self.uuid)
            self.elements = []
            self.signatures = []

    @property
    def mei(self):
        try:
            divisions = "".join([division.mei for division in self.elements])
            return f'<music><body><mdiv><score><scoreDef />' \
                   f'{divisions}' \
                   f'</score></mdiv></body></music>'
        except AttributeError:
            print(f"Document {self.uuid} has no attribute 'elements'. Len of children attribute: {len(self.elements)}")
            print(self.elements)
            return ""

    @property
    def json(self):
        return {"type": "chant", "elements": [division.json for division in self.elements]}





