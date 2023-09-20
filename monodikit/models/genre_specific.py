from dataclasses import dataclass
from .document import Chant, Division
import re

class Song(Chant):
    pass

class Sequence(Chant):
    pass

class OrdinaryChant(Chant):
    pass

class PlayPassage(Chant):
    pass


from .corpus import Corpus
class Play(Corpus):
    def __init__(self, directory, liturgical_play_id, sample=None, filters=None):
        def cummulative_filter(document_meta, source_meta):
            if document_meta["liturgical_play_id"] != liturgical_play_id:
                return False
            if filters:
                return filters(document_meta, source_meta)
        super().__init__(directory, sample=sample, filters=cummulative_filter)

class ProperTropeComplex(Chant):
    """
    A class representing a trope complex.

    Parameters
    ----------
    entry : str
        The entry to initialize the `ProperTropeComplex` object.

    Attributes
    ----------
    nums : list
        List of signatures of trope elements
    letters : list
        List of signatures of prima chant elements
    ct_volume : str or None
        The Corpus Troporum Volume
    ct_base_chant : str or None
        ...

    Methods
    -------
    get_ct_base_chant()
        Extracts the base chant from the `meta.bibliographischerverweis` attribute using regular expressions.
    get_ct_volume()
        Extracts the volume from the `meta.bibliographischerverweis` attribute using regular expressions.
    get_nums() -> list
        Extracts numbers from the `meta.bibliographischerverweis` attribute and returns them as a list of integers.
    get_letters() -> list
        Extracts uppercase letters from the `meta.bibliographischerverweis` attribute and returns them as a list of strings.
    get_trope_elements() -> list
        Returns a list of divisions from the `data.elements` attribute of the `Document` whose status is "Tropenelement".
    get_primechant_elements() -> list
        Returns a list of divisions from the `data.elements` attribute of the `Document` whose status is "Einsatzmarke" (prime chant elements).
    """

    def __init__(self, entry):
        super().__init__(entry)
        self.nums = self.get_nums()
        self.letters = self.get_letters()
        self.ct_volume = self.get_ct_volume()
        self.ct_base_chant = self.get_ct_base_chant()

    def get_ct_base_chant(self):
        base_chant_match = re.search(r'^.*?(?=\s(?:\d|A))', self.meta.bibliographical_reference)
        return base_chant_match.group(0) if base_chant_match else None

    def get_ct_volume(self):
        volume_match = re.search(r'\(CT\s(\w+)\)$', self.meta.bibliographical_reference)
        return volume_match.group(1) if volume_match else None

    def get_nums(self) -> list:
        return [int(number) for number in re.findall(r"\d+", self.meta.bibliographical_reference)]

    def get_letters(self) -> list:
        return [letter for letter in self.meta.bibliographical_reference.split() if
                len(letter) == 1 and letter.isupper()]

    def get_trope_elements(self):
        return [division for division in self.data.elements if division.status == "Tropenelement"]

    def get_primechant_elements(self):
        return [division for division in self.data.elements if
                division.status == "Einsatzmarke"]  # Does not distinguish between complete and abbreviated (Einsatzmarke) prime chant elements

@dataclass
class TropeElement(Division):
    """
    A dataclass representing a trope element, inheriting from the `Division` class.
    """
    pass

@dataclass
class PrimeChantElement(Division):
    """
    A dataclass representing a prime chant element, inheriting from the `Division` class.
    """
    pass
