from django.forms.widgets import ClearableFileInput

class MultiFileInput(ClearableFileInput):
    """File input that lets the browser send multiple files."""
    allow_multiple_selected = True
