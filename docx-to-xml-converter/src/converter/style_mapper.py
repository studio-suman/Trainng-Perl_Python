class StyleMapper:
    def __init__(self):
        self.style_mapping = {
            'Normal': 'normal',
            'Heading1': 'heading1',
            'Heading2': 'heading2',
            'Heading3': 'heading3',
            'ListParagraph': 'list',
            # Add more mappings as needed
        }

    def map_style(self, docx_style):
        """Maps a DOCX style to an XML style."""
        return self.style_mapping.get(docx_style, 'default')  # Return 'default' if style not found

    def get_all_mappings(self):
        """Returns all style mappings."""
        return self.style_mapping.items()