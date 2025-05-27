class XmlGenerator:
    def __init__(self):
        self.xml_content = ""

    def start_document(self):
        self.xml_content += "<?xml version='1.0' encoding='UTF-8'?>\n"
        self.xml_content += "<document>\n"

    def end_document(self):
        self.xml_content += "</document>\n"

    def add_paragraph(self, paragraph):
        self.xml_content += f"  <paragraph style='{paragraph.style}'>\n"
        self.xml_content += f"    {paragraph.text}\n"
        self.xml_content += "  </paragraph>\n"

    def add_table(self, table):
        self.xml_content += "  <table>\n"
        for row in table.rows:
            self.xml_content += "    <row>\n"
            for cell in row.cells:
                self.xml_content += f"      <cell>{cell.content}</cell>\n"
            self.xml_content += "    </row>\n"
        self.xml_content += "  </table>\n"

    def get_xml(self):
        return self.xml_content.strip()