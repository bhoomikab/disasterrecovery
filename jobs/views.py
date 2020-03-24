from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Job
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import JobForm
from user.decorators import admin_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

def home(request):
    return render(request, template_name='jobs/home.html')


@login_required
@admin_required
def JobDetails(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_details.html', {'jobs': jobs})


class JobCreate(CreateView):
    model = Job
    template_name = 'jobs/form.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs:job_details')

    def form_valid(self, form):
        return super(JobCreate, self).form_valid(form)


class JobDelete(DeleteView):
    model = Job
    template_name = 'jobs/job_delete.html'
    success_url = reverse_lazy('jobs:job_details')

    def form_valid(self, form):
        return super(JobDelete, self).form_valid(form)


class JobUpdate(UpdateView):
    model = Job
    template_name = 'jobs/form.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs:job_details')

    def form_valid(self, form):
        return super(JobUpdate, self).form_valid(form)
