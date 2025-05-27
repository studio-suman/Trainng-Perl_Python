# README.md

# DOCX to XML Converter

This project is a DOCX to XML converter that retains all UI elements such as styling, color, tables, and content. It provides a simple way to convert DOCX files into structured XML format while preserving the original document's formatting.

## Features

- Extracts content from DOCX files, including paragraphs, tables, and styles.
- Generates XML representations of the extracted content.
- Maps DOCX styles to XML styles to ensure formatting is retained.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the converter, run the following command:

```
python src/main.py <path_to_docx_file>
```

Replace `<path_to_docx_file>` with the path to the DOCX file you want to convert.

## Directory Structure

```
docx-to-xml-converter
├── src
│   ├── main.py
│   ├── converter
│   │   ├── __init__.py
│   │   ├── docx_parser.py
│   │   ├── xml_generator.py
│   │   └── style_mapper.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── document.py
│   │   ├── paragraph.py
│   │   └── table.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── tests
│   ├── __init__.py
│   ├── test_docx_parser.py
│   ├── test_xml_generator.py
│   └── test_style_mapper.py
├── requirements.txt
└── setup.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.