from django.conf.urls import url
from .views import JobDetails, JobCreate, JobDelete, JobUpdate
from .models import Job
from .forms import JobForm

urlpatterns = [
    url(r'^$', JobDetails, name='job_details'),
    url(r'^create/$', JobCreate.as_view(), name='job_create'),
    url(r'^delete/(?P<pk>\d+)/$', JobDelete.as_view(), name='job_delete'),
    url(r'^update/(?P<pk>\d+)/$',
        JobUpdate.as_view(
            model=Job,
            template_name='jobs/form.html',
            form_class=JobForm),
        name='job_edit'),
]
