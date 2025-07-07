# posts/forms.py
from django import forms
from .models import Post, Image

class MultipleFileInput(forms.ClearableFileInput):   # ← 1-line subclass
    allow_multiple_selected = True                  # enable “multiple”

class PostForm(forms.ModelForm):
    # images = forms.FileField(
    #     required=False,
    #     widget=MultipleFileInput(attrs={"multiple": True}),
    #     help_text="Upload images (max 2 MB each)",
    # )

    # pic = forms.FileField(widget = forms.TextInput(attrs={
    #     "name": "images",
    #     "type": "File",
    #     "class": "form-control",
    #     "multiple": "True",
    # }), label = "")

    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
            "required": "False",
        }), label = "")
    # class Meta:
    #     model = Image
    #     fields = ['pic']

    class Meta:
        model  = Post
        fields = ["title", "body", 'pic' ]

    # size + type validation
    def clean_images(self):
        files = self.files.getlist("images")
        for f in files:
            if not f.content_type.startswith("image/"):
                raise forms.ValidationError(f"{f.name} isn’t an image.")
            if f.size > 2 * 1024 * 1024:
                raise forms.ValidationError(f"{f.name} exceeds 2 MB.")
        return files
