from django import forms
from django.core.exceptions import ValidationError

class MultiFileField(forms.FileField):
    """
    FileField that accepts 0‑N uploaded files and returns a list of files.
    """
    def clean(self, data, initial=None):
        if data in self.empty_values:
            return []

        # Browser may send a single file or list; coerce to list
        if not isinstance(data, (list, tuple)):
            data = [data]

        cleaned, errors = [], []
        for f in data:
            try:
                # Re‑use FileField’s built‑in checks for each file
                super().clean(f, initial)
                cleaned.append(f)
            except ValidationError as e:
                errors.extend(e.error_list)

        if errors:
            raise ValidationError(errors)

        return cleaned
