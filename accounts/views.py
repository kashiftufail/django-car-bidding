# accounts/views.py
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import UpdateView
# from django.urls import reverse_lazy
# from .forms import UserProfileForm

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     form_class  = UserProfileForm
#     template_name = "accounts/profile_form.html"
#     success_url   = reverse_lazy("profile_edit")

#     def get_object(self):
#         return self.request.user.profile
    

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import ProfileForm

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("profile_edit")

    def get_object(self):
        return self.request.user.profile
    
    
    
     



