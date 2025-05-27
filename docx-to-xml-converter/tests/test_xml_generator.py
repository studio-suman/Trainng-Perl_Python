import unittest
from src.converter.xml_generator import XmlGenerator
from src.models.document import Document
from src.models.paragraph import Paragraph
from src.models.table import Table

class TestXmlGenerator(unittest.TestCase):

    def setUp(self):
        self.xml_generator = XmlGenerator()

    def test_generate_xml_for_paragraph(self):
        paragraph = Paragraph(text="Sample paragraph", style="Normal")
        xml_output = self.xml_generator.generate_xml(paragraph)
        expected_output = "<paragraph style='Normal'>Sample paragraph</paragraph>"
        self.assertEqual(xml_output, expected_output)

    def test_generate_xml_for_table(self):
        table = Table(rows=[
            ["Header 1", "Header 2"],
            ["Row 1 Col 1", "Row 1 Col 2"]
        ])
        xml_output = self.xml_generator.generate_xml(table)
        expected_output = "<table><row><cell>Header 1</cell><cell>Header 2</cell></row><row><cell>Row 1 Col 1</cell><cell>Row 1 Col 2</cell></row></table>"
        self.assertEqual(xml_output, expected_output)

    def test_generate_xml_for_document(self):
        document = Document(paragraphs=[
            Paragraph(text="First paragraph", style="Normal"),
            Paragraph(text="Second paragraph", style="Normal")
        ])
        xml_output = self.xml_generator.generate_xml(document)
        expected_output = "<document><paragraph style='Normal'>First paragraph</paragraph><paragraph style='Normal'>Second paragraph</paragraph></document>"
        self.assertEqual(xml_output, expected_output)

if __name__ == '__main__':
    unittest.main()