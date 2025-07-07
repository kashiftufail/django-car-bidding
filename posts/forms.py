from django import forms
from .models import Post
from images.models import Image
from .fields import MultiFileField
from .widgets import MultiFileInput

class PostForm(forms.ModelForm):
    uploaded_images = MultiFileField(
        widget=MultiFileInput(attrs={"multiple": True}),
        required=False,
        label="Upload image(s)",
        help_text="JPEG/PNG • ≤ 2 MB each",
    )

    class Meta:
        model  = Post
        fields = ["title", "body", "uploaded_images"]

    # capture current user once
    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    # per‑file validation
    def clean_uploaded_images(self):
        files = self.cleaned_data["uploaded_images"]  # list from MultiFileField
        for f in files:
            if not f.content_type.startswith("image/"):
                raise forms.ValidationError(f"{f.name} isn’t an image.")
            if f.size > 2 * 1024 * 1024:
                raise forms.ValidationError(f"{f.name} exceeds 2 MB.")
        return files

    # save post then its images
    def save(self, commit=True):
        post = super().save(commit=commit)
        for f in self.cleaned_data["uploaded_images"]:
            Image.objects.create(file=f, uploaded_by=self.user, post=post)
        return post
