from django import forms
from .models import UserProfile
from images.models import Image
from allauth.account.forms import SignupForm
from roles.models import Role
from accounts.thread_locals import set_signup_role

class ProfileForm(forms.ModelForm):
    avatar_file = forms.ImageField(
        required=False,
        label="Upload New Avatar"
    )

    class Meta:
        model = UserProfile
        fields = ['phone', 'info', 'city', 'state', 'zip', 'role']

    def save(self, commit=True, user=None):
        profile = super().save(commit=False)
        if self.cleaned_data.get("avatar_file"):
            uploaded_image = Image.objects.create(
                file=self.cleaned_data["avatar_file"],
                uploaded_by=profile.user
            )
            profile.avatar = uploaded_image

        if commit:
            profile.save()
        return profile
    

# from django import forms

class CustomSignupForm(SignupForm):
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        label="Register as"
    )

    def save(self, request):
        selected_role = self.cleaned_data['role']
        set_signup_role(selected_role)
        return super().save(request)    