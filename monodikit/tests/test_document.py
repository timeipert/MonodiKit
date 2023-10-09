import unittest
from unittest.mock import MagicMock, patch
from models.corpus import Corpus, create_document, check_files_exist
from models.document import Chant, NeumeComponent, Syllable, Neume, Meta, Data
from models.genre_specific import ProperTropeComplex
import tests.mock_data as mock

class TestNeume(unittest.TestCase):

    def test_calculate_number(self):
        neume = NeumeComponent("uuid", "C", False, "Normal", 4, False, (0,))
        self.assertEqual(neume.calculate_number(), 29)  # (4 * 7) + 3 = 29

    def test_parse_neume_content_flat(self):
        # Mock spaced_element for a flat note
        spaced_element = {
            "nonSpaced": [{"grouped": [{"uuid": "..",
                                        "focus": False,
                                        "noteType": "Flat",
                                        "base": "F", "octave": 3,
                                        "liquescent": False}]}],
        }

        neume = Neume(spaced_element, (0,))

        # Ensure neume has accidentals
        self.assertTrue(neume.accidentals)
        self.assertEqual(len(neume.accidentals), 1)

    def test_mei_generation(self):
        # Mock spaced_element for a normal note
        spaced_element = {
            "nonSpaced": [{"grouped": [{"uuid": "..",
                                        "focus": False,
                                        "noteType": "Normal",
                                        "base": "C", "octave": 4,
                                        "liquescent": False}]}],
        }

        neume = Neume(spaced_element, (0,))

        expected_mei = '<neume><nc pname="c" oct="4"/></neume>'
        self.assertEqual(neume.mei, expected_mei)


class TestSyllable(unittest.TestCase):
    def test_get_neumes(self):
        syllable = Syllable("uuid", "kind", (1,), "text", "Normal", mock.notes_data, False, False, True)
        self.assertEqual(len(syllable.neumes), 1)

    def test_mei_generation(self):
        syllable = Syllable("uuid", "kind", (0,), "text", "Normal", mock.notes_data, False, False, True, )
        expected_mei = '<syllable><syl>text</syl><neume><nc pname="c" oct="4"/></neume></syllable>'
        self.assertEqual(syllable.mei, expected_mei)


