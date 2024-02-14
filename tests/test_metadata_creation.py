import unittest
from unittest.mock import MagicMock, patch
from monodikit.models.source import Source
from monodikit.models.document import Meta
import tests.mock_data as mock

class TestMeta(unittest.TestCase):
    def test_document_meta(self):
        m = Meta(**mock.doc_meta_mock)
        self.assertEqual(m.source_id, "Apt 17")
        self.assertEqual(m.unknown,  {'unknownvalue': 'test'} )
    def test_source_meta(self):
        m = Source(**mock.source_meta_mock)
        self.assertEqual(m.sigle, "Apt 17")
        self.assertEqual(m.publish, True)
        self.assertEqual(m.unknown,  {'unknownvalue': 'test'} )


if __name__ == '__main__':
    unittest.main()