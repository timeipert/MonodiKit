import unittest
from unittest.mock import MagicMock, patch
from monodikit.models.corpus import Corpus, create_document, check_files_exist
from monodikit.models.document import Chant, NeumeComponent, Syllable, Neume, Meta, Data
from monodikit.models.genre_specific import ProperTropeComplex
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


class TestVolpiano(unittest.TestCase):
    def test_one_doc(self):
        ground_truth = ['d', 'e', 'd', 'c', 'f', 'e', 'd', 'e', 'g', 'h', 'i', 'j', 'h', 'g', 'h', 'g', 'g', 'f', 'e', 'd', 'd', 'e', 'd',
         'c', 'f', 'g', 'f', 'e', 'd', 'e', 'g', 'h', 'i', 'j', 'h', 'g', 'f', 'e', 'd', 'e', 'f', 'e', 'd', 'c', 'd', 'h',
         'g', 'h', 'l', 'l', 'h', 'e', 'f', 'g', 'g', 'f', 'e', 'd', 'e', 'd', 'e', 'g', 'i', 'h', 'j', 'h', 'g', 'f', 'e',
         'd', 'c', 'e', 'f', 'e', 'd', 'c', 'd', 'd', 'f', 'h', 'd', 'e', 'd', 'c', 'g', 'e', 'd', 'l', 'l', 'h', 'k', 'j',
         'h', 'g', 'h', 'e', 'f', 'g', 'f', 'e', 'd', 'e', 'd', 'e', 'g', 'g', 'h', 'd', 'e', 'f', 'e', 'd', 'c', 'e', 'd',
         'e', 'f', 'e', 'd', 'c', 'd', 'd', 'f', 'g', 'h', 'i', 'j', 'h', 'g', 'f', 'e', 'd', 'f', 'e', 'c', 'd', 'f', 'g',
         'h', 'i', 'j', 'h', 'g', 'f', 'e', 'd', 'f', 'e', 'c', 'd', 'e', 'g', 'f', 'g', 'f', 'e', 'd', 'e', 'c', 'd', 'e',
         'f', 'g', 'f', 'e', 'd', 'e', 'd', 'e', 'g', 'f', 'g', 'e', 'd', 'e', 'c', 'd', 'e', 'f', 'g', 'f', 'e', 'd', 'e',
         'd', 'h', 'h', 'f', 'g', 'e', 'd', 'e', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'h', 'g', 'f', 'e', 'd', 'd', 'e', 'f',
         'e', 'd', 'c', 'd', 'h', 'h', 'f', 'g', 'e', 'd', 'e', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'h', 'g', 'f', 'e', 'd',
         'd', 'e', 'f', 'e', 'd', 'c', 'd', 'c', 'e', 'g', 'h', 'g', 'h', 'j', 'l', 'k', 'j', 'l', 'j', 'h', 'h', 'g', 'f',
         'e', 'd', 'e', 'd', 'd', 'e', 'f', 'e', 'd', 'c', 'e', 'f', 'g', 'f', 'e', 'd', 'e', 'd', 'c', 'e', 'g', 'h', 'g',
         'h', 'j', 'l', 'k', 'j', 'l', 'j', 'h', 'h', 'f', 'e', 'd', 'e', 'd', 'd', 'e', 'f', 'e', 'd', 'c', 'e', 'f', 'g',
         'f', 'e', 'd', 'e', 'd', 'c', 'e', 'g', 'h', 'g', 'h', 'j', 'k', 'j', 'h', 'l', 'j', 'h', 'h', 'd', 'h', 'k', 'j',
         'g', 'h', 'g', 'f', 'f', 'e', 'd', 'd', 'e', 'f', 'e', 'd', 'd', 'c', 'c', 'e', 'g', 'f', 'g', 'e', 'd', 'c', 'e',
         'g', 'h', 'g', 'h', 'j', 'k', 'j', 'h', 'l', 'j', 'h', 'h', 'd', 'h', 'h', 'k', 'j', 'g', 'h', 'g', 'f', 'f', 'e',
         'd', 'd', 'e', 'f', 'e', 'd', 'c', 'e', 'g', 'h', 'g', 'g', 'e', 'd', 'd', 'e', 'g', 'h', 'd', 'e', 'd', 'c', 'g',
         'f', 'e', 'd']
        doc = create_document(mock.chant_data["entry_path"])
        self.assertEqual(doc.volpiano, ground_truth)


