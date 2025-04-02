from docx import Document
from docx.shared import Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Sample dataframe data for demonstration
def generate_docx(df):
    data = [
        {
            'Name': df['Name'],
            'Email': df['Email'],
            'Phone': df['Phone'],
            'Education': df['Education'],
            'Experience': df['Experience'],
            'Skills': df['Skills']
        },
    ]

    # Create a new Document
    doc = Document()

    # Add a table with two columns
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False

    # Set the width of the columns
    table.columns[0].width = Inches(2)
    table.columns[1].width = Inches(4)

    # Add header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Field"
    hdr_cells[1].text = "Details"

    # Add data to the table
    for entry in data:
        for key, value in entry.items():
            row_cells = table.add_row().cells
            row_cells[0].text = key
            row_cells[1].text = value

    # Add left side panel with custom formatting
    for row in table.rows:
        cell = row.cells[0]
        cell.width = Inches(2)
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), "D9D9D9")  # Light grey color
        cell._element.get_or_add_tcPr().append(shading_elm)

    # Save the document
    doc.save("custom_resume_template.docx")

    print("The custom DOCX boiler template has been created and saved as custom_resume_template.docx.")