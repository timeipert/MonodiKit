import unittest
from unittest.mock import MagicMock, patch
from monodikit.models.corpus import Corpus, create_document, check_files_exist
from monodikit.models.document import Chant
from monodikit.models.genre_specific import ProperTropeComplex
import tests.mock_data as mock

class TestCorpus(unittest.TestCase):

    def test_create_document(self):
        # Mock data for the document creation
        entry = mock.chant_data["entry_path"]
        filters = lambda x, y: True  # Mock filter function
        sources = {"source_id": "Test"}  # Mock sources

        # Mock Chant class
        result = create_document(entry, filters, sources)
        self.assertIsInstance(result, Chant)  # Check instance type


    # Add more test cases for the Corpus class functionality

if __name__ == '__main__':
    unittest.main()
