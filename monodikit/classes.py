from dataclasses import dataclass, field
import re, json, glob, os, random
from typing import List
from xml.sax.saxutils import escape



@dataclass
class TropeElement(Division):
    pass



@dataclass
class PrimeChantElement(Division):
    pass

@dataclass
class NeumeComponent:
    uuid: str
    base: str
    liquescent: str
    noteType: str
    octave: int
    focus: bool
    index: int

    @property
    def pitch(self):
        return self.base + str(self.octave)

    @property
    def mei(self):
        if self.index == 0:
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
                return NeumeComponent(**element, index=index)
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

class Leveler:
    def __init__(self, documentType):
        docTypeToLevel = {"Level1": 1, "Level2": 2, "Level3": 3}
        self.levels = docTypeToLevel[documentType]
        self.current_level = 0

    def next_level(self):
        if self.levels < self.current_level:
            self.current_level += 1
            return True
        else:
            return False

    @property
    def interdivision(self):
        if self.levels > self.current_level:
            return True
        else:
            return False


@dataclass
class Division:
    """
    A class representing a division of a medieval chant document.
    """
    data: list  #: A list of data elements for the division.
    children: list  #: A list of child elements for the division.
    level: Leveler #: Does it contain content or another division?

    # syllables : list = field(init=False)

    def __post_init__(self):
        if self.level.interdivision:
            self.level.next_level()
            self.elements = [Division(d["data"], d["children"], self.level) for d in self.children]
            self.signatures: List[str] = [e.signature for e in self.elements]
        else:
            self.signature: str = self.get_signature()  #: The signature of the division, if present.
            self.status: str = self.get_status()  #: The status of the division, if present.
            self.syllables: list = self.get_syllables()  #: A list of `Syllable` objects representing the syllables in the division.

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

    def get_number_of_levels(self):
        pass

    def filter_paratexts(self, children):
        return [child for child in children if child["kind"] != "ParatextContainer"]

    def get_syllables(self):
        return [Syllable(**d) for child in self.filter_paratexts(self.children)
                for d in child["children"]
                ]

    def get_flat_neumes(self):
        return [neume
                for syllable in self.syllables
                for neume in syllable.neumes]

    def get_flat_neume_components(self):
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


class Document:
    """
    A class representing a document or unit of medieval chant.

    A document is represented by its metadata and data,
    which are loaded from JSON files located in a directory specified
    by the entry parameter.
    """

    def __init__(self, entry_path):
        self.meta = self.get_meta(entry_path)
        self.data = self.get_data(entry_path)
        self.type = self.meta.gattung1  #: The type of the document, taken from the gattung1 attribute of its metadata.

    @staticmethod
    def get_meta(entry_path):
        if glob.glob(entry_path + "/meta.json"):
            with open(entry_path + "/meta.json") as f:
                meta = Meta(**json.load(f))
            return meta
        else:
            return None

    @staticmethod
    def get_data(entry):
        if glob.glob(entry + "/data.json"):
            with open(entry + "/data.json") as f:
                data = Data(**json.load(f))
            return data
        else:
            return None

    def get_flat_syllables(self):
        return [syllable
                for division in self.data.elements
                for syllable in division.syllables]

    def get_flat_neumes(self):
        return [neume
                for division in self.data.elements
                for neume in division.get_flat_neumes()]

    def get_flat_neume_components(self):
        return [note_component
                for division in self.data.elements
                for note_component in division.get_flat_neume_components()]

    @property
    def mei(self):
        return f'<?xml version="1.0" encoding="UTF-8"?>' \
               '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" ' \
               'type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>' \
               '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" ' \
               'type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>' \
               '<mei xmlns="http://www.music-encoding.org/ns/mei"><meiHead><fileDesc><titleStmt>' \
               '<title></title></titleStmt><pubStmt></pubStmt></fileDesc></meiHead>' \
               f'{self.data.mei}' \
               '</mei>'

    @property
    def json(self):
        return self.data.json


class Lied:
    pass


class Paratext:
    pass


@dataclass
class Meta:
    id: str
    quelle_id: str
    dokumenten_id: str
    gattung1: str
    gattung2: str
    festtag: str
    feier: str
    textinitium: str
    bibliographischerverweis: str
    druckausgabe: str
    zeilenstart: int
    foliostart: str
    kommentar: str
    editionsstatus: str
    additionalData: dict



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
        self.elements = [Division(d["data"], d["children"], Leveler(self.documentType)) for d in self.children]
        self.signatures: List[str] = [e.signature for e in self.elements]

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


class ProperTropeComplex(Document):
    """
    A class representing a trope complex.

    A `TropeComplex` is created by loading a `Document` object into it.
    If the `Document` object's `type` attribute is "Tropus",
    its metadata and data are used to create a `TropeComplex` object.
    Otherwise, an exception is raised.
    """

    def __init__(self, entry):
        super().__init__(entry)
        self.nums = self.get_nums()
        self.letters = self.get_letters()
        self.ct_volume = self.get_ct_volume()
        self.ct_base_chant = self.get_ct_base_chant()

    def get_ct_base_chant(self):
        base_chant_match = re.search(r'^.*?(?=\s(?:\d|A))', self.meta.bibliographischerverweis)
        return base_chant_match.group(0) if base_chant_match else None

    def get_ct_volume(self):
        volume_match = re.search(r'\(CT\s(\w+)\)$', self.meta.bibliographischerverweis)
        return volume_match.group(1) if volume_match else None

    def get_nums(self) -> list:
        return [int(number) for number in re.findall(r"\d+", self.meta.bibliographischerverweis)]

    def get_letters(self) -> list:
        return [letter for letter in self.meta.bibliographischerverweis.split() if
                len(letter) == 1 and letter.isupper()]

    def get_trope_elements(self):
        return [division for division in self.data.elements if division.status == "Tropenelement"]

    def get_primechant_elements(self):
        return [division for division in self.data.elements if
                division.status == "Einsatzmarke"]  # Does not distinguish between complete and abbreviated (Einsatzmarke) prime chant elements


class Corpus:
    def __init__(self, directory, sample=False):
        self.directory = directory
        self.documents = self.load_corpus(sample)

    def load_corpus(self, sample):
        if not sample:
            return [self.create_document(entry) for source in glob.glob(self.directory)
                    for entry in
                    [directory for directory in glob.glob(os.path.join(source, "*")) if os.path.isdir(directory)]]
        else:
            entries = [entry for source in glob.glob(self.directory)
                       for entry in
                       [directory for directory in glob.glob(os.path.join(source, "*")) if os.path.isdir(directory)]]
            return [self.create_document(entry) for entry in random.sample(entries, sample)]

    @staticmethod
    def create_document(entry):
        """
        Creates a new instance of a document. At first checks for a specific type and assigns a genre-specific subclass
        (for example TropeComplex()). If no suitable subclass is found, it returns a generic Document() instance.
        """
        meta = Document.get_meta(entry)
        if meta.gattung1 == "Tropus":
            return ProperTropeComplex(entry)
        # ... other genres
        else:
            return Document(entry)

