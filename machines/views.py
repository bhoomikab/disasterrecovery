from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user.decorators import admin_required
from .models import Machine
from .forms import MachineForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

@login_required
@admin_required
def MachineDetails(request):
    machines = Machine.objects.all()
    return render(request, 'machines/machine_details.html', {'machines': machines})


class MachineCreate(CreateView):
    model = Machine
    template_name = 'machines/form.html'
    form_class = MachineForm
    success_url = reverse_lazy('machines:machine_details')

    def form_valid(self, form):
        return super(MachineCreate, self).form_valid(form)


class MachineDelete(DeleteView):
    model = Machine
    template_name = 'machines/machine_delete.html'
    success_url = reverse_lazy('machines:machine_details')

    def form_valid(self, form):
        return super(MachineDelete, self).form_valid(form)


class MachineUpdate(UpdateView):
    model = Machine
    template_name = 'machines/form.html'
    form_class = MachineForm
    success_url = reverse_lazy('machines:machine_details')

    def form_valid(self, form):
        return super(MachineUpdate, self).form_valid(form)
