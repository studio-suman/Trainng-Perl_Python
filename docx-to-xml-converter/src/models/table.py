class Table:
    def __init__(self, rows):
        self.rows = rows  # List of rows, where each row is a list of cells

    def to_xml(self):
        xml = '<table>\n'
        for row in self.rows:
            xml += '  <row>\n'
            for cell in row:
                xml += f'    <cell>{cell}</cell>\n'
            xml += '  </row>\n'
        xml += '</table>'
        return xml