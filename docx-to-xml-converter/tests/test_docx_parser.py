import unittest
from src.converter.docx_parser import DocxParser

class TestDocxParser(unittest.TestCase):

    def setUp(self):
        self.parser = DocxParser()

    def test_extract_paragraphs(self):
        # Test extraction of paragraphs from a sample DOCX file
        paragraphs = self.parser.extract_paragraphs('sample.docx')
        self.assertIsInstance(paragraphs, list)
        self.assertGreater(len(paragraphs), 0)

    def test_extract_tables(self):
        # Test extraction of tables from a sample DOCX file
        tables = self.parser.extract_tables('sample.docx')
        self.assertIsInstance(tables, list)
        self.assertGreater(len(tables), 0)

    def test_extract_styles(self):
        # Test extraction of styles from a sample DOCX file
        styles = self.parser.extract_styles('sample.docx')
        self.assertIsInstance(styles, dict)
        self.assertIn('Heading1', styles)

if __name__ == '__main__':
    unittest.main()