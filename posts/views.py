from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib import messages
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = "posts"
    login_url = "/accounts/login/"

class PostDetail(DetailView):
    model = Post
    slug_field = "slug"
    slug_url_kwarg = "slug"

# class PostCreate(CreateView):
#     model = Post
#     fields = ["title", "body"]
#     success_url = reverse_lazy("post_list")

#     def form_valid(self, form):
#         messages.success(self.request, "Post created successfully!")
#         return super().form_valid(form)


    
class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = "posts/post_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        print("Form is valid, saving post...")
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form) 

    def form_invalid(self, form):
        print("Form is innnnnnn valid, saving post...")

        messages.error(self.request, "There was an error creating the post.")
        return super().form_invalid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model        = Post
    form_class   = PostForm
    slug_field   = "slug"
    slug_url_kwarg = "slug"

    def form_valid(self, form):
        response = super().form_valid(form)

        # Attach any newly-uploaded images
        for file in self.request.FILES.getlist("images"):
            image = Image.objects.create(file=file, uploaded_by=self.request.user)
            self.object.images.add(image)

        messages.success(self.request, "Post updated.")
        return redirect(self.object.get_absolute_url())

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("post_list")
