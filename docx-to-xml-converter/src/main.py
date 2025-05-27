import argparse
from converter.docx_parser import DocxParser
from converter.xml_generator import XmlGenerator
from converter.style_mapper import StyleMapper

def main():
    parser = argparse.ArgumentParser(description='Convert DOCX files to XML format.')
    parser.add_argument('input_file', type=str, help='Path to the input DOCX file')
    parser.add_argument('output_file', type=str, help='Path to the output XML file')
    
    args = parser.parse_args()

    # Initialize the parser, style mapper, and XML generator
    docx_parser = DocxParser()
    style_mapper = StyleMapper()
    xml_generator = XmlGenerator()

    # Parse the DOCX file
    document = docx_parser.parse(args.input_file)

    # Map styles
    style_mapper.map_styles(document)

    # Generate XML
    xml_content = xml_generator.generate(document)

    # Write the XML content to the output file
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)

if __name__ == '__main__':
    main()