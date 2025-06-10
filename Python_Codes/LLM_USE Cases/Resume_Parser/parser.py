from docx import Document
from docxtpl import DocxTemplate

def extract_resume_data(doc_path):
    doc = Document(doc_path)
    data = {
        "name": "",
        "email": "",
        "phone": "",
        "education": "",
        "experience": ""
    }

    current_label = None
    label_map = {
        "name": "Name",
        "email": "Email",
        "phone": "Phone",
        "education": "Education",
        "experience": "Experience"
    }

    for para in doc.paragraphs:
        text = para.text.strip().replace('\u00a0', ' ')  # Normalize non-breaking spaces
        lower_text = text.lower()

        # Check if the paragraph starts with a known label
        for label in label_map:
            if lower_text.startswith(label + ":"):
                value = text.split(":", 1)[-1].strip()
                if value:
                    data[label_map[label]] = value
                    current_label = None
                else:
                    current_label = label_map[label]
                break
        else:
            # If the previous line was a label and this line is the value
            if current_label and text:
                data[current_label] = text
                current_label = None

    return data

def fill_template(template_path, output_path, data):
    template = DocxTemplate(template_path)
    template.render(data)
    template.save(output_path)

# File paths
resume_path = r"D:\OneDrive - Wipro\Desktop\sample_resume.docx"
template_path = r"D:\OneDrive - Wipro\Desktop\Placeholder.docx"
output_path = r"D:\OneDrive - Wipro\Desktop\output_resume.docx"

# Process
resume_data = extract_resume_data(resume_path)
print("Extracted Data:", resume_data)

# Fill the template
# fill_template(template_path, output_path, resume_data)
print(f"Resume has been parsed and the output is saved to {output_path}.")