from django.conf.urls import url
from .views import MachineDetails, MachineCreate, MachineDelete, MachineUpdate
from .forms import MachineForm
from .models import Machine

urlpatterns = [
    url(r'^$', MachineDetails, name='machine_details'),
    url(r'^create/$', MachineCreate.as_view(), name='machine_create'),
    url(r'^delete/(?P<pk>\d+)/$', MachineDelete.as_view(), name='machine_delete'),
    url(r'^update/(?P<pk>\d+)/$',
        MachineUpdate.as_view(
            model=Machine,
            template_name='jobs/form.html',
            form_class=MachineForm),
        name='machine_edit'),
]
