import glob
import json
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union
from xml.sax.saxutils import escape
import functools

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Accidental:
    uuid: str
    base: str
    liquescent: bool
    noteType: str
    octave: int
    focus: bool
    index: Tuple[int, ...]  # index is a tuple of ints

    @property
    def mei(self) -> str:
        """
        Returns an MEI <accid> element string for this accidental.
        """
        if self.noteType == "Flat":
            accid = "f"
        elif self.noteType == "Natural":
            accid = "n"
        else:
            accid = "?"
        # Use self.octave (not self.oct). Escape base in case of special characters.
        return (
            f'<accid ploc="{escape(self.base)}" poct="{self.octave}" accid="{accid}"/>'
        )

    @property
    def volpiano(self) -> Optional[str]:
        """
        Returns the Volpiano code for this accidental, if defined.
        """
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
        return None

    @property
    def json(self) -> Dict[str, str]:
        """
        Returns a JSON-serializable dict representation of this accidental.
        """
        return {"type": "accidental", "pitch": f"{self.base}{self.octave}"}


@functools.total_ordering
@dataclass
class NeumeComponent:
    uuid: str
    base: str
    liquescent: bool
    noteType: str
    octave: int
    focus: bool
    index: Tuple[int, ...]  # index is a tuple of ints

    # Class-level mappings (constants)
    note_to_num: Dict[str, int] = field(
        default_factory=lambda: {"C": 1, "D": 2, "E": 3, "F": 4, "G": 5, "A": 6, "B": 7},
        init=False,
        repr=False,
    )
    volpiano_matching: Dict[str, str] = field(
        default_factory=lambda: {
            "F3": "8", "G3": "9", "A3": "a", "B3": "b",
            "C4": "c", "D4": "d", "E4": "e", "F4": "f",
            "G4": "g", "A4": "h", "B4": "j", "C5": "k",
            "D5": "l", "E5": "m", "F5": "n", "G5": "o",
            "A5": "p", "B5": "q", "C6": "r", "D6": "s", "E6": "t",
        },
        init=False,
        repr=False,
    )
    chantdigger_matching: Dict[str, str] = field(
        default_factory=lambda: {
            "F3": "F", "G3": "G", "A3": "A", "B3": "H",
            "C4": "c", "D4": "d", "E4": "e", "F4": "f",
            "G4": "g", "A4": "a", "B4": "h", "C5": "c'",
            "D5": "d'", "E5": "e'", "F5": "f'", "G5": "g'",
            "A5": "a'", "B5": "h'", "C6": "c''", "D6": "d''", "E6": "e''",
        },
        init=False,
        repr=False,
    )
    _numeric_val: int = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """
        Compute a numeric value for ordering purposes.
        """
        try:
            self._numeric_val = self.octave * 7 + self.note_to_num[self.base]
        except KeyError:
            logger.warning(f"Unknown base '{self.base}' in NeumeComponent indexing.")
            self._numeric_val = self.octave * 7

    def calculate_number(self) -> int:
        """
        Returns the numeric value used for comparing this component's pitch.
        """
        return self._numeric_val

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, NeumeComponent):
            return NotImplemented
        return (self._numeric_val, self.liquescent) == (other._numeric_val, other.liquescent)

    def __lt__(self, other: "NeumeComponent") -> bool:
        return self._numeric_val < other._numeric_val

    @property
    def pitch(self) -> str:
        """
        Returns a string like "C4" representing this component's pitch.
        """
        return f"{self.base}{self.octave}"

    @property
    def volpiano(self) -> str:
        """
        Returns the Volpiano code for this pitch, or "?" if not found.
        """
        code = self.volpiano_matching.get(self.pitch)
        if code is None:
            logger.warning(f"Volpiano not found for pitch {self.pitch}. Returning '?' instead.")
            return "?"
        return code

    @property
    def chantdigger(self) -> str:
        """
        Returns the ChantDigger code for this pitch, or "?" if not found.
        """
        code = self.chantdigger_matching.get(self.pitch)
        if code is None:
            logger.warning(f"ChantDigger not found for pitch {self.pitch}. Returning '?' instead.")
            return "?"
        return code

    @property
    def mei(self) -> str:
        """
        Returns an MEI <nc> element (with optional <liquescent/> or other inner tags).
        """
        # Determine if "con" attribute is needed
        con = "" if self.index[-1] == 0 else ' con="g"'
        pname = escape(self.base.lower())
        oct_attr = str(self.octave)

        if self.liquescent:
            inner = "<liquescent/>"
        elif self.noteType != "Normal":
            # noteType might be something like "Flat" or "Natural"; wrap it in a tag
            inner = f"<{self.noteType}/>"
        else:
            inner = ""

        return f'<nc pname="{pname}" oct="{oct_attr}"{con}>{inner}</nc>'

    @property
    def json(self) -> Dict[str, str]:
        """
        Returns a JSON-serializable dict for this note component.
        """
        return {"type": "note", "pitch": self.pitch}

    def __str__(self) -> str:
        return f"<NeumeComponent base={self.base}, oct={self.octave}>"

    def __repr__(self) -> str:
        return self.__str__()


@dataclass
class EmptyNeumeComponent(NeumeComponent):
    @property
    def pitch(self) -> str:
        return "Empty"

    @property
    def mei(self) -> str:
        return ""  # No MEI output for an empty component


class Neume:
    """
    A class representing a neume (a group of notes) loosely following the MEI specification.
    """

    def __init__(self, spaced_element: Dict[str, Any], index: Tuple[int, ...]) -> None:
        self.index: Tuple[int, ...] = index
        self.neume_content: List[Union[NeumeComponent, Accidental]] = self.get_neume_content(spaced_element)
        # Separate the content into components vs. accidentals
        self.neume_components: List[NeumeComponent] = [
            element for element in self.neume_content if isinstance(element, NeumeComponent)
        ]
        self.accidentals: List[Accidental] = [
            element for element in self.neume_content if isinstance(element, Accidental)
        ]

    def parse_neume_content(
        self, element: Dict[str, Any], idx: Tuple[int, ...]
    ) -> Optional[Union[NeumeComponent, Accidental]]:
        """
        Parse a single grouped element (connected_neume_component) into either a NeumeComponent,
        an Accidental, or None (if filtered out).
        """
        try:
            note_type = element.get("noteType")
            if note_type == "Normal":
                neume = NeumeComponent(**element, index=idx)
                low_peak = NeumeComponent(
                    uuid="", base="G", liquescent=False, noteType="Normal", octave=3, focus=False, index=idx
                )
                comment_note = NeumeComponent(
                    uuid="", base="A", liquescent=True, noteType="Normal", octave=5, focus=False, index=idx
                )
                # If below G3 or equal to comment note, filter out
                if neume < low_peak or neume == comment_note:
                    return None
                return neume
            elif note_type in {"Flat", "Natural"}:
                return Accidental(**element, index=idx)
            else:
                return None
        except Exception as ex:
            logger.warning(f"Failed to parse neume content at {idx}: {ex}")
            return None

    def get_neume_content(self, spaced_element: Dict[str, Any]) -> List[Union[NeumeComponent, Accidental]]:
        """
        For a given 'spaced' element dict, parse all 'nonSpaced' → 'grouped' sublists,
        flatten them, and return all valid NeumeComponent or Accidental objects.
        """
        content: List[Optional[Union[NeumeComponent, Accidental]]] = []
        try:
            non_spaced_list = spaced_element.get("nonSpaced", [])
            for index1, neume_group in enumerate(non_spaced_list):
                grouped_list = neume_group.get("grouped", [])
                for index2, component_dict in enumerate(grouped_list):
                    idx = self.index + (index1 + index2,)
                    parsed = self.parse_neume_content(component_dict, idx)
                    if parsed is not None:
                        content.append(parsed)
        except Exception as ex:
            logger.error(f"Could not parse neume content for spaced_element {self.index}: {ex}")
        return content

    @property
    def mei(self) -> str:
        """
        Returns the combined MEI XML string for this neume (accidentals first, then <neume> wrapper).
        """
        neume_components_xml = "".join(nc.mei for nc in self.neume_components)
        accidentals_xml = "".join(acc.mei for acc in self.accidentals) if self.accidentals else ""
        return f"{accidentals_xml}<neume>{neume_components_xml}</neume>"

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dict for this neume.
        """
        return {"type": "neume", "elements": [el.json for el in self.neume_content]}

    @property
    def volpiano(self) -> str:
        """
        Returns the Volpiano string for all components in this neume.
        """
        return "".join(nc.volpiano for nc in self.neume_components)

    def chantdigger(self) -> str:
        """
        Returns the ChantDigger string for all components in this neume.
        """
        return " ".join(nc.chantdigger for nc in self.neume_components)


@dataclass
class Syllable:
    uuid: str
    kind: str
    index: Tuple[int, ...]
    text: str = ""
    syllableType: str = ""
    notes: Dict[str, Any] = field(default_factory=dict)
    endsWord: bool = False
    focus: bool = False
    hasNotes: Optional[bool] = None

    # 'neumes' is initialized in __post_init__
    neumes: List[Neume] = field(init=False)

    def __post_init__(self) -> None:
        """
        After initialization, parse 'notes' into a list of Neume objects if syllableType is "Normal".
        """
        if self.syllableType == "Normal":
            self.neumes = self.get_neumes(self.notes)
        else:
            self.neumes = []

    def get_neumes(self, notes: Dict[str, Any]) -> List[Neume]:
        """
        Given a 'notes' dict (which should contain a 'spaced' key), return a list of Neume objects.
        """
        if "spaced" not in notes:
            return []
        neumes_out: List[Neume] = []
        try:
            for index, neume_dict in enumerate(notes["spaced"]):
                neumes_out.append(Neume(neume_dict, self.index + (index,)))
        except Exception as ex:
            logger.warning(f"Error parsing neumes for syllable at {self.index}: {ex}")
        return neumes_out

    @property
    def mei(self) -> str:
        """
        Returns the MEI XML string for this syllable (<syllable> wrapper with <syl> and contained neumes).
        """
        neumes_xml = "".join(neume.mei for neume in self.neumes)
        escaped_text = escape(self.text)
        return f"<syllable><syl>{escaped_text}</syl>{neumes_xml}</syllable>"

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dict for this syllable.
        """
        return {"type": "syllable", "lyric": self.text, "elements": [n.json for n in self.neumes]}

    @property
    def volpiano(self) -> str:
        """
        Returns a Volpiano string for all neumes in this syllable, separated by hyphens.
        """
        return "".join(f"{neume.volpiano}-" for neume in self.neumes)

    def chantdigger(self) -> str:
        """
        Returns the ChantDigger string in the format "[text] pitches..."
        """
        melody_parts = "".join(neume.chantdigger() for neume in self.neumes)
        return f"[{self.text}] {melody_parts}"


@dataclass
class EditorialLine:
    """
    A class representing one editorial line (staff + layer) in a division.
    """
    uuid: str
    kind: str
    children: List[Dict[str, Any]]
    index: Tuple[int, ...]
    text: str = ""

    # 'syllables' is initialized in __post_init__
    syllables: List[Syllable] = field(init=False)

    def __post_init__(self) -> None:
        self.syllables = self.get_syllables()

    @staticmethod
    def filter_clefs(children: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Remove any child dicts where kind == "Clef".
        """
        return [child for child in children if child.get("kind") != "Clef"]

    def get_syllables(self) -> List[Syllable]:
        """
        Parse children (excluding clefs) into Syllable objects.
        """
        out: List[Syllable] = []
        try:
            for idx, child in enumerate(self.filter_clefs(self.children)):
                out.append(Syllable(**child, index=self.index + (idx,)))
        except Exception as ex:
            logger.warning(f"Error parsing syllables at EditorialLine {self.index}: {ex}")
        return out

    @property
    def mei(self) -> str:
        """
        Return the MEI XML for this editorial line (<staff><layer>...).
        """
        if not self.syllables:
            return ""
        content = "".join(syllable.mei for syllable in self.syllables)
        return f"<staff><layer>{content}</layer></staff>"

    @property
    def volpiano(self) -> str:
        """
        Return the Volpiano string for all syllables in this line.
        """
        return "".join(f"{s.volpiano}-" for s in self.syllables)

    @property
    def chantdigger(self) -> str:
        """
        Return the ChantDigger string for all syllables in this line.
        """
        return " ".join(s.chantdigger() for s in self.syllables)


@dataclass
class Division:
    """
    A class representing a division (section) of a medieval chant document.
    """
    data: List[Dict[str, Any]]
    children: List[Dict[str, Any]]
    index: Tuple[int, ...]

    # Initialized in __post_init__
    elements: List["Division"] = field(init=False)
    editorial_lines: List[EditorialLine] = field(init=False)
    interdivision: bool = field(init=False)
    signature: Optional[str] = field(init=False)
    status: Optional[str] = field(init=False)

    def __post_init__(self) -> None:
        """
        Determine if this division contains sub-divisions (interdivision) or is a leaf.
        If it has sub-divisions, recursively build them. Otherwise, parse editorial lines.
        """
        self.elements = []
        self.editorial_lines = []
        children_wo_paratext = self.filter_paratexts(self.children)

        # If any child has both "data" and "children", treat as interdivision
        if any("data" in child and "children" in child for child in children_wo_paratext):
            self.interdivision = True
            for idx, div in enumerate(children_wo_paratext):
                child_data = div.get("data", [])
                child_children = div.get("children", [])
                self.elements.append(
                    Division(child_data, child_children, self.index + (idx,))
                )
            self.editorial_lines = self.get_flat_editorial_lines()
        else:
            self.interdivision = False
            self.editorial_lines = self.get_editorial_lines()

        self.signature = self.get_signature()
        self.status = self.get_status()

    def get_signature(self) -> Optional[str]:
        """
        Extract "Signatur" from this division's data list, if present.
        """
        division_metadata = {d.get("name"): d.get("data") for d in self.data}
        return division_metadata.get("Signatur")

    def get_status(self) -> Optional[str]:
        """
        Extract "Status" from this division's data list, if present.
        """
        dd = {d.get("name"): d.get("data") for d in self.data}
        return dd.get("Status")

    @staticmethod
    def filter_paratexts(children: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Remove any child where kind == "ParatextContainer".
        """
        return [child for child in children if child.get("kind") != "ParatextContainer"]

    def get_editorial_lines(self) -> List[EditorialLine]:
        """
        Parse direct children (excluding paratexts) into EditorialLine objects.
        """
        out: List[EditorialLine] = []
        for idx, child in enumerate(self.filter_paratexts(self.children)):
            try:
                out.append(EditorialLine(**child, index=self.index + (idx,)))
            except Exception as ex:
                logger.warning(f"Could not parse editorial line at {self.index + (idx,)}: {ex}")
        return out

    def get_flat_editorial_lines(self) -> List[EditorialLine]:
        """
        If this is an interdivision, gather all editorial lines from nested divisions.
        """
        flat_lines: List[EditorialLine] = []
        if self.elements:
            for div in self.elements:
                if div.interdivision:
                    flat_lines.extend(div.get_flat_editorial_lines())
                else:
                    flat_lines.extend(div.editorial_lines)
        return flat_lines

    @property
    def flat_syllables(self) -> List[Syllable]:
        """
        Return all Syllable objects in this division.
        """
        return [
            syllable
            for e_l in self.editorial_lines
            for syllable in e_l.syllables
        ]

    @property
    def flat_neumes(self) -> List[Neume]:
        """
        Return all Neume objects in this division.
        """
        return [
            neume
            for e_l in self.editorial_lines
            for syllable in e_l.syllables
            for neume in syllable.neumes
        ]

    @property
    def flat_neume_components(self) -> List[Union[NeumeComponent, Accidental]]:
        """
        Return all NeumeComponent and Accidental objects in this division.
        """
        components: List[Union[NeumeComponent, Accidental]] = []
        for e_l in self.editorial_lines:
            for syllable in e_l.syllables:
                for neume in syllable.neumes:
                    components.extend(neume.neume_content)
        return components

    @property
    def mei(self) -> str:
        """
        Returns the MEI XML string for this division (either nested <section> or a leaf).
        """
        if self.elements:
            # Interdivision: wrap child divisions
            inner = "".join(div.mei for div in self.elements)
            return f"<section>{inner}</section>"
        elif self.editorial_lines:
            # Leaf division: wrap editorial lines
            inner = "".join(el.mei for el in self.editorial_lines)
            return f"<section>{inner}</section>"
        return ""

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dict for this division.
        """
        return {"type": "section", "elements": [syll.json for syll in self.flat_syllables]}

    @property
    def volpiano(self) -> str:
        """
        Returns the Volpiano string for all editorial lines in this division.
        """
        return "".join(el.volpiano for el in self.editorial_lines)

    @property
    def chantdigger(self) -> str:
        """
        Returns the ChantDigger string for all editorial lines in this division.
        """
        return "".join(el.chantdigger for el in self.editorial_lines)


class Chant:
    """
    A class representing a document or unit of medieval chant.
    Initializes from a directory containing 'meta.json' and 'data.json'.
    """

    def __init__(self, entry_path: str) -> None:
        self.meta = self.get_meta(entry_path)
        data = self.get_data(entry_path)
        if data:
            self.data = data
        else:
            raise FileNotFoundError(f"Could not load data.json for entry: {entry_path}")
        self.type = self.meta.genre  # e.g., genre from metadata

    @staticmethod
    def get_meta(entry_path: str) -> "Meta":
        """
        Reads 'meta.json' in the given directory and returns a Meta instance.
        """
        meta_files = glob.glob(f"{entry_path}/meta.json")
        if meta_files:
            try:
                with open(meta_files[0], "r", encoding="utf-8") as f:
                    metadata = json.load(f)
                return Meta(**metadata)
            except TypeError as missing_docs:
                logger.error(
                    f"Loading Metadata was not successful; TypeError: {missing_docs}. "
                    f"Loaded metadata: {metadata}"
                )
                raise
        else:
            raise FileNotFoundError(f"meta.json not found in {entry_path}")

    @staticmethod
    def get_data(entry_path: str) -> Optional["Data"]:
        """
        Reads 'data.json' in the given directory and returns a Data instance.
        """
        data_files = glob.glob(f"{entry_path}/data.json")
        if data_files:
            with open(data_files[0], "r", encoding="utf-8") as f:
                try:
                    data_dict = json.load(f)
                    return Data(**data_dict)
                except TypeError as ex:
                    logger.error(f"Error loading data.json: {ex}")
                    raise
        return None

    @property
    def flat_syllables(self) -> List[Syllable]:
        """
        All Syllable objects across all divisions in this chant.
        """
        return [
            syllable
            for division in self.data.elements
            for e_l in division.editorial_lines
            for syllable in e_l.syllables
        ]

    @property
    def flat_text(self) -> str:
        """
        Concatenate all syllable texts (lyrics) into a single string.
        """
        return " ".join(s.text for s in self.flat_syllables)

    @property
    def flat_neumes(self) -> List[Neume]:
        """
        All Neume objects across all divisions in this chant.
        """
        return [
            neume
            for division in self.data.elements
            for neume in division.flat_neumes
        ]

    @property
    def flat_neume_components(self) -> List[Union[NeumeComponent, Accidental]]:
        """
        All NeumeComponent and Accidental objects across all divisions.
        """
        try:
            return [
                comp
                for division in self.data.elements
                for comp in division.flat_neume_components
            ]
        except Exception as e:
            logger.warning(f"Warning in Chant.flat_neume_components: {e}")
            return []

    @property
    def volpiano(self) -> str:
        """
        Build a multi-line Volpiano string, one line per division.
        """
        return "".join(f"{division.volpiano}\n" for division in self.data.elements)

    @property
    def chantdigger(self) -> str:
        """
        Concatenates metadata and ChantDigger-encoded melody lyrics.
        """
        melody = "".join(division.chantdigger for division in self.data.elements)
        return (
            f"{self.meta.initial_text}\n"
            f"{self.meta.genre}\n"
            f"{self.meta.bibliographical_reference}\n"
            f"{melody}\n"
            f"{self.flat_text}\n"
        )

    @property
    def pitches(self) -> List[str]:
        """
        List of all pitch strings (e.g., "C4") across the chant.
        """
        return [comp.pitch for comp in self.flat_neume_components]

    @property
    def syllable_text(self) -> List[str]:
        """
        List of all syllable texts (lyrics) across the chant.
        """
        return [s.text for s in self.flat_syllables]

    @property
    def flat_neume_components_by_division(self) -> List[List[Union[NeumeComponent, Accidental]]]:
        """
        Returns a nested list: for each division, a list of NeumeComponent/Accidental objects.
        """
        return [div.flat_neume_components for div in self.data.elements]

    @property
    def mei(self) -> str:
        """
        Returns a complete MEI document string for this chant, including the MEI header.
        """
        try:
            divisions_xml = "".join(div.mei for div in self.data.elements)
            return (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" '
                'type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>'
                '<?xml-model href="https://music-encoding.org/schema/dev/mei-Neumes.rng" '
                'type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>'
                '<mei xmlns="http://www.music-encoding.org/ns/mei">'
                "<meiHead><fileDesc><titleStmt><title></title></titleStmt><pubStmt></pubStmt></fileDesc></meiHead>"
                f"{self.data.mei}"
                "</mei>"
            )
        except Exception as e:
            logger.warning(f"Warning: Could not get MEI for document {self.meta.document_id}: {e}")
            return ""

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dict representation of the entire chant data.
        """
        return self.data.json


class Meta:
    """
    Metadata for a chant, loaded from meta.json.
    """

    def __init__(
        self,
        id: str,
        quelle_id: str,
        dokumenten_id: str,
        gattung1: str,
        gattung2: str,
        festtag: str,
        feier: str,
        textinitium: str,
        bibliographischerverweis: str,
        druckausgabe: str,
        zeilenstart: str,
        foliostart: str,
        kommentar: str,
        editionsstatus: str,
        additionalData: Dict[str, Any],
        **kw: Any,
    ) -> None:
        self.uuid = id
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
        self.condition_of_transmission = additionalData.get("Überlieferungszustand", "")
        self.iiif_urls = additionalData.get("iiifs", "")

        # Capture any unexpected extra fields
        self.unknown = kw

    @property
    def as_record(self) -> Dict[str, Any]:
        """
        Return a flat dictionary of metadata fields.
        """
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
            "iiif_urls": self.iiif_urls,
        }


@dataclass
class Data:
    """
    A class representing the JSON 'data' section of a chant document.
    """
    comments: List[Dict[str, Any]]
    uuid: str
    kind: str
    children: List[Dict[str, Any]]
    documentType: str
    elements: List[Division] = field(init=False, default_factory=list)
    signatures: List[Optional[str]] = field(init=False, default_factory=list)
    version: str = ""
    globalComment: Any = ""

    def __post_init__(self) -> None:
        """
        Parse each child that has 'data' and 'children' into a Division.
        """
        try:
            for idx, divisions in enumerate(self.children):
                if "data" in divisions and "children" in divisions:
                    self.elements.append(
                        Division(divisions["data"], divisions["children"], (idx,))
                    )
            self.signatures = [e.signature for e in self.elements]
        except Exception as e:
            logger.warning(f"Element parsing did not work for Data uuid={self.uuid}: {e}")
            self.elements = []
            self.signatures = []

    @property
    def mei(self) -> str:
        """
        Returns the MEI XML for this data section (wrapped in <music><body><mdiv><score>).
        """
        try:
            divisions_xml = "".join(div.mei for div in self.elements)
            return (
                "<music><body><mdiv><score><scoreDef/>"
                f"{divisions_xml}"
                "</score></mdiv></body></music>"
            )
        except AttributeError as e:
            logger.warning(
                f"Warning: Document {self.uuid} has no attribute 'elements'. "
                f"Error: {e}"
            )
            return ""

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dict for this data section.
        """
        return {"type": "chant", "elements": [div.json for div in self.elements]}
