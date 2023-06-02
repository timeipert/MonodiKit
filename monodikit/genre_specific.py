from dataclasses import dataclass
from document import Document, Division
import re

class Lied:
    pass

class Sequence:
    pass

class OrdinaryChant:
    pass

class LiturgicalPlay:
    pass

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

@dataclass
class TropeElement(Division):
    pass

@dataclass
class PrimeChantElement(Division):
    pass
