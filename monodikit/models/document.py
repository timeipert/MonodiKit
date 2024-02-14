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
    index: tuple

    @property
    def mei(self):
        if self.noteType == "Flat":
            accid = "f"
        elif self.noteType == "Natural":
            accid = "n"
        else:
            accid = "?"

        return f'<accid ploc="{self.base}" poct="{self.oct}" accid="{accid}"'

    @property
    def volpiano(self):
        if self.noteType == "Flat":
            if self.base == "B":
                return "i"
            if self.base == "E" and self.octave == 4:
                return "w"
            if self.base == "E" and self.octave == 5:
                return "x"
        elif self.noteType == "Natural":
            if self.base == "B":
                return "I"
            if self.base == "E" and self.octave == 4:
                return "W"
            if self.base == "E" and self.octave == 5:
                return "X"

    @property
    def json(self):
        return {"type": "accidental", "pitch": f"{self.base}{self.octave}"}


@dataclass
class NeumeComponent:
    uuid: str
    base: str
    liquescent: bool
    noteType: str
    octave: int
    focus: bool
    index: tuple
    note_to_num = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
    volpiano_matching = {"F3": "8", "G3": "9", "A3": "a", "B3": "b", "C4": "c", "D4": "d", "E4": "e", "F4": "f",
                         "G4": "g", "A4": "h", "B4": "j", "C5": "k", "D5": "l", "E5": "m", "F5": "n", "G5": "o",
                         "A5": "p", "B5": "q", "C6": "r", "D6": "s"}

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
    def volpiano(self):
        return self.volpiano_matching[self.pitch]

    @property
    def mei(self):
        if self.index[-1] == 0:
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

    @property
    def pitch(self):
        return f"{self.base}{self.octave}"

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

    def __init__(self, spaced_element, index):  #: Takes a dictionary representing the spaced element of the neume.
        self.index = index
        self.neume_content = self.get_neume_content(spaced_element)  #: A list of `NeumeComponent` objects.
        self.neume_components = [element for element in self.neume_content if type(element) == NeumeComponent]
        self.accidentals = [element for element in self.neume_content if type(element) == Accidental]

    """Parses NeumeComponents and Accidentals within a Neume object."""
    def parse_neume_content(self, element, index):
        try:
            if element["noteType"] == "Normal":
                neume = NeumeComponent(**element, index=self.index + (index,))
                low_peak = NeumeComponent(uuid="", base="G", liquescent=False, noteType="Normal", octave=3, focus=False,
                                          index=self.index + (0,))
                comment_note = NeumeComponent(uuid="", base="A", liquescent=True, noteType="Normal", octave=5,
                                              focus=False, index=self.index + (0,))
                if neume < low_peak or neume == comment_note:
                    # return EmptyNeumeComponent(**element, index=self.index + (index,))
                    return None
                else:
                    return neume
            elif element["noteType"] == "Flat" or element.noteType == "Natural":
                return Accidental(**element, index=self.index + (index,))
        except AttributeError:
            return None

    """Wraps whole content up into a list"""
    def get_neume_content(self, spaced_element):
        try:
            return [neume for neume in [self.parse_neume_content(connected_neume_component, (index1 + index2))
                                       for index2, neume_component in enumerate(spaced_element["nonSpaced"])
                                       for index1, connected_neume_component in enumerate(neume_component["grouped"])] if
                    neume is not None]
        except Exception as ex:
            print("Error: Could not parse neume content: ", type(ex), ex.args, spaced_element)
            return []

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
        return {"type": "neume", "elements": [neume_components.json for neume_components in self.neume_content]}

    @property
    def volpiano(self):
        return "".join([nc.volpiano for nc in self.neume_components])

@dataclass
class Syllable:
    uuid: str
    kind: str
    index: tuple
    text: str = ""
    syllableType: str = ""
    notes: dict = field(default_factory=dict)  # Notes good terminology? includes groups etc.
    endsWord: bool = False
    focus: bool = False
    hasNotes: bool = None
    neumes: list = field(init=False)  # How to name elements / notes? notes is now input, elements the

    # processed Notes instance
    def __post_init__(self):
        if self.syllableType == "Normal":
            self.neumes = self.get_neumes(self.notes)
        else:
            self.neumes = []

    def get_neumes(self, notes):
        if "spaced" not in notes:
            return []
        try:
            return [Neume(neume, self.index + (index,)) for index, neume in enumerate(notes["spaced"])]
        except Exception as ex:
            print("Error: Could not parse neumes: ", type(ex), ex.args, notes)
            return []

    @property
    def mei(self):
        neumes = "".join([neume.mei for neume in self.neumes])
        return f"<syllable><syl>{escape(self.text)}</syl>{neumes}</syllable>"

    @property
    def json(self):
        return {"type": "syllable", "lyric": self.text, "elements": [neume.json for neume in self.neumes]}

    @property
    def volpiano(self):
        return "".join([f"{neume.volpiano}-" for neume in self.neumes])

@dataclass
class EditorialLine:
    """
    A class representing a Editorial Line associated with the textual phrases.
    """
    uuid: str
    kind: str
    children: list
    index: tuple

    def __post_init__(self):
        self.syllables = self.get_syllables()

    @staticmethod
    def filter_clefs(children):
        return [child for child in children if child["kind"] != "Clef"]

    def get_syllables(self):
        try:
            return [Syllable(**div, index=self.index + (index,))
                    for index, div in enumerate(EditorialLine.filter_clefs(self.children))
                    ]
        except Exception as ex:
            print("Error: Could not parse syllables: ", type(ex), ex.args, self.children)
            return []

    @property
    def mei(self):
        if len(self.syllables) == 0:
            return ""
        syllables = "".join([syllable.mei for syllable in self.syllables])
        return f"<staff><layer>{syllables}</layer></staff>"

    @property
    def volpiano(self):
        return "".join([f"{syllable.volpiano}-" for syllable in self.syllables])

@dataclass
class Division:
    """
    A class representing a division of a medieval chant document.
    """
    data: list  #: A list of data elements for the division.
    children: list  #: A list of child elements for the division.
    index: tuple

    def __post_init__(self):
        self.elements = []
        self.editorial_lines = []
        children_wo_paratext = self.filter_paratexts(self.children)
        if "data" in [keys for child in children_wo_paratext for keys in child.keys()]:

            self.interdivision = True
            self.elements = [Division(div["data"], div["children"], self.index + (index,)) for index, div in
                             enumerate(children_wo_paratext)]
            self.editorial_lines: list = self.get_flat_editorial_lines()
        else:
            self.interdivision = False
            self.elements = []
            self.editorial_lines: list = self.get_editorial_lines()  #: A list of `Syllable` objects representing the syllables in the division.

            # print("syllables", self.syllables)

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

    def get_editorial_lines(self):
        editorial_lines = []
        for index, child in enumerate(self.filter_paratexts(self.children)):
            try:
                editorial_lines.append(EditorialLine(**child, index=self.index + (index,)))
            except Exception as ex:
                print("Error: Could not parse editorial line: ", type(ex), ex.args, child[0:20])
        return editorial_lines

    def get_flat_editorial_lines(self):
        if len(self.elements):
            if self.elements[0].interdivision:
                return [editorial_line for division in self.elements for editorial_line in
                        division.get_flat_editorial_lines()]
            else:
                return [editorial_line for division in self.elements for editorial_line in division.editorial_lines]
        else:
            return []

    @property
    def flat_syllables(self):
        """ Get a list of syllables within a division. """
        return [syllable
                for editorial_line in self.editorial_lines
                for syllable in editorial_line.syllables]

    @property
    def flat_neumes(self):
        """ Get a list of neumes within a division. """
        return [neume
                for editorial_line in self.editorial_lines
                for syllable in editorial_line.syllables
                for neume in syllable.neumes]

    @property
    def flat_neume_components(self):
        """ Get a list of neume components within a division. """
        return [note_component
                for editorial_line in self.editorial_lines
                for syllable in editorial_line.syllables
                for neume in syllable.neumes
                for note_component in neume.neume_content]
        # if c["kind"] == "Syllable"


    @property
    def mei(self):
        if len(self.elements) > 0:
            division = "".join([division.mei for division in self.elements])
            return f"<section>{division}</section>"
        elif len(self.editorial_lines) > 0:
            editorial_line = "".join([e_l.mei for e_l in self.editorial_lines])
            return f"<section>{editorial_line}</section>"

    @property
    def json(self):
        return {"type": "section", "elements": [syllable.json for syllable in self.flat_syllables]}

    # def get_linechange(self):
    #     return [ Syllable(c) for child in self.children for d in child["children"] for c in d["children"] ]

    @property
    def volpiano(self):
        return "".join([syllable.volpiano for syllable in self.editorial_lines])
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
                for el in division.editorial_lines
                for syllable in el.syllables]

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
            print('Warning for Chant property flat_neume_components: '
                  'data.elements is None at: ', self.meta.dokumenten_id)
            return []

    @property
    def volpiano(self):
        return "".join([f"{division.volpiano}\n" for division in self.data.elements])

    @property
    def pitches(self):
        return [note_component.pitch for note_component in self.flat_neume_components]

    @property
    def syllable_text(self):
        return [syllable.text for syllable in self.flat_syllables]

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
            print("Warning: Could not get MEI for: ", self.meta.dokumenten_id)
            return ""

    @property
    def json(self):
        return self.data.json




class Meta:

    def __init__(self, id, quelle_id, dokumenten_id, gattung1, gattung2, festtag, feier, textinitium,
                 bibliographischerverweis, druckausgabe, zeilenstart, foliostart, kommentar, editionsstatus,
                 additionalData, **kw):
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
        self.iiif_urls = additionalData.get("iiifs", "")

        self.unknown = kw

    @property
    def as_record(self):
        return {
            "uuid": self.uuid,
            "source_id": self.source_id,
            "document_id": self.document_id,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "feast_day": self.feast_day,
            "feast_time": self.feast_time,
            "initial_text": self.initial_text,

            "initial_folio": self.initial_folio,
            "initial_line": self.initial_line,
            "ending_folio": self.ending_folio,
            "ending_line": self.ending_line,

            "bibliographical_reference": self.bibliographical_reference,
            "cm_volume": self.cm_volume,

            "editorial_comment": self.editorial_comment,
            "melody_number": self.melody_number,
            "melodyname_standardized": self.melodyname_standardized,
            "melodyname_diplomatic": self.melodyname_diplomatic,
            "editor": self.editor,
            "related_chant": self.related_chant,
            "liturgical_play_id": self.liturgical_play_id,
            "completeness": self.completeness,
            "layer_of_addendum": self.layer_of_addendum,
            "condition_of_transmission": self.condition_of_transmission,
            "iiif_urls": self.iiif_urls
        }


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
        # try:
        self.elements = [Division(divisions["data"], divisions["children"], (index,)) for index, divisions in
                         enumerate(self.children) if "data" in divisions and "children" in divisions]
        self.signatures: List[str] = [e.signature for e in self.elements]

    # except:
    #    print("Element parsing did not work with doc: ", self.uuid)
    #    self.elements = []
    #    self.signatures = []

    @property
    def mei(self):
        try:
            divisions = "".join([division.mei for division in self.elements])
            return f'<music><body><mdiv><score><scoreDef />' \
                   f'{divisions}' \
                   f'</score></mdiv></body></music>'
        except AttributeError as e:

            print(f"Warning: Document {self.uuid} has no attribute 'elements'. Len of children attribute: {len(self.elements)}")
            print(f"Elements content is: ", self.elements)
            print("Original error message: ", e)

            return ""

    @property
    def json(self):
        return {"type": "chant", "elements": [division.json for division in self.elements]}


