# cars/forms.py
from django import forms
from .models import Car
import datetime
from images.models import Image
from posts.fields import MultiFileField
from posts.widgets import MultiFileInput
from variant.models import Variant
from make.models import Make

YEAR_CHOICES = [(year, year) for year in range(1970, datetime.datetime.now().year + 1)]

class CarForm(forms.ModelForm):
    manufacture_year = forms.ChoiceField(choices=YEAR_CHOICES, label="Manufacture Year")

    uploaded_images = MultiFileField(
        widget=MultiFileInput(attrs={"multiple": True}),
        required=False,
        label="Upload image(s)",
        help_text="JPEG/PNG • ≤ 2 MB each",
    )

    make = forms.ModelChoiceField(
        queryset=Make.objects.all(),
        required=True,
        label="Make"
    )

    variant = forms.ModelChoiceField(
        queryset=Variant.objects.none(),  # initially empty, filled by JS
        required=True,
        label="Variant"
    )


    class Meta:
        model = Car
        fields = ["make", "variant", "title", "detail", "uploaded_images","manufacture_year", "odometer",
                  "car_type", "fuel_type", "has_keys", "engine_starts"]

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["variant"].queryset = Variant.objects.filter(make=self.instance.variant.make)
        elif 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['variant'].queryset = Variant.objects.filter(make_id=make_id)
            except (ValueError, TypeError):
                self.fields['variant'].queryset = Variant.objects.none()
        else:
            self.fields['variant'].queryset = Variant.objects.none()    

    def clean_uploaded_images(self):
        files = self.cleaned_data["uploaded_images"]
        for f in files:
            if not f.content_type.startswith("image/"):
                raise forms.ValidationError(f"{f.name} isn’t an image.")
            if f.size > 2 * 1024 * 1024:
                raise forms.ValidationError(f"{f.name} exceeds 2 MB.")
        return files

    def save(self, commit=True):
        breakpoint()
        car = super().save(commit=False)
        
        if self.user:
            car.seller = self.user.profile
        if commit:
            car.save()
            for f in self.cleaned_data["uploaded_images"]:
                Image.objects.create(file=f, uploaded_by=self.user, car=car)
        return car
