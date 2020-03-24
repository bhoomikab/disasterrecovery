from django.conf.urls import url
from .views import UserDetails

urlpatterns = [
    url(r'^$', UserDetails, name='user_details'),

]
