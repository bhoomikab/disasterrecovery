from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import User
from .forms import AdminSignupForm, ContractorSignupForm
from .decorators import admin_required


# Create your views here.

class AdminSignupView(CreateView):
    model = User
    form_class = AdminSignupForm
    template_name = 'registration/signup_form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('jobs:job_details')

        if user is None:
            login(request, user)


class ContractorSignupView(CreateView):
    model = User
    form_class = ContractorSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'contractor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('jobs:job_details')

        if user is None:
            login(request, user)


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def UserDetails(request):
    users = User.objects.all()
    return render(request, 'user/user_details.html', {'users': users})
