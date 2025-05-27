class Document:
    def __init__(self):
        self.paragraphs = []
        self.tables = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def add_table(self, table):
        self.tables.append(table)

    def to_xml(self):
        # Convert the document structure to XML format
        xml_content = "<document>"
        for paragraph in self.paragraphs:
            xml_content += paragraph.to_xml()
        for table in self.tables:
            xml_content += table.to_xml()
        xml_content += "</document>"
        return xml_content