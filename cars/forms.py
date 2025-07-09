# cars/forms.py
from django import forms
from .models import Car
from images.models import Image
from posts.fields import MultiFileField
from posts.widgets import MultiFileInput

class CarForm(forms.ModelForm):
    uploaded_images = MultiFileField(
        widget=MultiFileInput(attrs={"multiple": True}),
        required=False,
        label="Upload image(s)",
        help_text="JPEG/PNG • ≤ 2 MB each",
    )

    class Meta:
        model = Car
        fields = ["title", "detail", "uploaded_images"]

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_uploaded_images(self):
        files = self.cleaned_data["uploaded_images"]
        for f in files:
            if not f.content_type.startswith("image/"):
                raise forms.ValidationError(f"{f.name} isn’t an image.")
            if f.size > 2 * 1024 * 1024:
                raise forms.ValidationError(f"{f.name} exceeds 2 MB.")
        return files

    def save(self, commit=True):
        car = super().save(commit=False)
        if self.user:
            car.seller = self.user.profile
        if commit:
            car.save()
            for f in self.cleaned_data["uploaded_images"]:
                Image.objects.create(file=f, uploaded_by=self.user, car=car)
        return car
