import mammoth
with open(r"D:\OneDrive - Wipro\Desktop\Template for Customv1.dotx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value

print(html)
with open("Doc2HTML.html", "w") as html_file:
    html_file.write(html)