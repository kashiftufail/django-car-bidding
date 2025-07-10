from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Car
from .forms import CarForm
from django.contrib import messages



class CarListView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    paginate_by = 3
    queryset = Car.objects.select_related('seller__user').prefetch_related('images').order_by('-id')



class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars:car_list')

    def form_valid(self, form):
        form.instance.seller = self.request.user.profile
        response = super().form_valid(form)
        messages.success(self.request, "Car added successfully!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

class CarDetailView(DetailView):  # public
    model = Car
    # breakpoint()
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        car = self.get_object()

        context['user'] = user
        context['user_profile'] = getattr(user, 'profile', None)
        context['show_bid_button'] = user.is_authenticated and hasattr(user, 'profile') and user.profile.role.name == 'bidder'

        # Load user's existing bid for this car
        bid = None
        if context['show_bid_button']:
            bid = car.bids.filter(user=user).first()
        context['has_bid'] = bid is not None
        context['existing_bid'] = bid
        return context

class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars:car_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.get_object().seller == self.request.user.profile

    def form_valid(self, form):
        form.instance.seller = self.request.user.profile
        return super().form_valid(form)

class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars:car_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.get_object().seller == self.request.user.profile
