import unittest
from src.converter.style_mapper import StyleMapper

class TestStyleMapper(unittest.TestCase):

    def setUp(self):
        self.style_mapper = StyleMapper()

    def test_map_style(self):
        docx_style = 'Heading1'
        expected_xml_style = 'h1'
        mapped_style = self.style_mapper.map_style(docx_style)
        self.assertEqual(mapped_style, expected_xml_style)

    def test_map_nonexistent_style(self):
        docx_style = 'NonExistentStyle'
        expected_xml_style = 'p'  # Default mapping for unknown styles
        mapped_style = self.style_mapper.map_style(docx_style)
        self.assertEqual(mapped_style, expected_xml_style)

    def test_map_multiple_styles(self):
        styles = ['Normal', 'Heading1', 'Heading2']
        expected_xml_styles = ['p', 'h1', 'h2']
        mapped_styles = [self.style_mapper.map_style(style) for style in styles]
        self.assertEqual(mapped_styles, expected_xml_styles)

if __name__ == '__main__':
    unittest.main()