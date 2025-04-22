import json
import pdfkit

def generate_resume(data):

    # Parse JSON data
    resume = json.loads(data)

    # Convert JSON to HTML
    html_content = f"""
    <html>
    <head>
    <title>Resume</title>
    </head>
    <body>
    <h1>{resume['name']}'s Resume</h1>
    <p><strong>Email:</strong> {resume['email']}</p>
    <p><strong>Phone:</strong> {resume['phone']}</p>
    <h2>Summary</h2>
    <p>{resume['summary']}</p>
    <h2>Skills</h2>
    <ul>
    """
    for skill in resume['skills']:
        html_content += f"<li>{skill}</li>"
    html_content += "</ul>"
    html_content += "<h2>Experience</h2>"
    for exp in resume['experience']:
        html_content += f"<h3>{exp['title']} at {exp['company']} ({exp['duration']})</h3>"
        html_content += "<ul>"
        for resp in exp['responsibilities']:
            html_content += f"<li>{resp}</li>"
        html_content += "</ul>"
    html_content += f"<h2>Education</h2><p>{resume['education']}</p>"
    html_content += """
    </body>
    </html>
    """

    # Convert HTML to PDF
    pdfkit.from_string(html_content, f'Resume-{resume['name']}.pdf')

    print("PDF created successfully!")



