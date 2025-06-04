import json
from re import A
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_resume(data):

    # Parse JSON data
    resume = json.loads(data)

    # Create a PDF with ReportLab
    c = canvas.Canvas(f"Resume-{resume['name']}.pdf", pagesize=letter)
    width, height = letter  # Keep track of the page size

    c.setFont("Helvetica", 12)
    y_position = height - 50  # Start 50 pixels down from the top

    # Function to add lines of text
    def add_line(text, height_offset=15):
        nonlocal y_position
        y_position -= height_offset
        c.drawString(50, y_position, text)

    # Add content
    add_line(f"Name: {resume['name']}")
    add_line(f"Email: {resume['email']}")
    add_line(f"Phone: {resume['phone']}")
    add_line("Summary:")
    add_line(resume['summary'], height_offset=30)

    # Skills
    add_line("Skills:")
    skills = ', '.join(resume['skills'])
    add_line(skills, height_offset=30)

    # Experience
    add_line("Experience:")
    for exp in resume['experience']:
        add_line(f"{exp['title']} at {exp['company']} ({exp['duration']})", height_offset=20)
        # for resp in exp['responsibilities']:
        #     add_line(f"- {resp}", height_offset=15)
        y_position -= 10  # Extra space after each block

    # Education
    add_line(f"Education: {resume['education']}")
    

    add_line("Additional Information:")
    add_line(resume.get('additional_info', 'N/A'), height_offset=30)

    # Save the PDF
    c.save()

    return bool