# images/forms.py

from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ObjectDoesNotExist

class ImageInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def save_new(self, form, commit=True):
        obj = super().save_new(form, commit=False)
        # breakpoint()
        if self.request and not obj.uploaded_by_id:
            try:
                obj.uploaded_by = self.request.user
            except ObjectDoesNotExist:
                obj.uploaded_by = None  # fallback if no userprofile
        if commit:
            obj.save()
        return obj
