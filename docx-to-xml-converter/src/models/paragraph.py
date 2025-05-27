class Paragraph:
    def __init__(self, text, style=None):
        self.text = text
        self.style = style

    def to_xml(self):
        style_attr = f' style="{self.style}"' if self.style else ''
        return f'<p{style_attr}>{self.text}</p>'