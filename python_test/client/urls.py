from django.conf.urls import url
from .views import *

app_name = 'clients'

urlpatterns = [
    url(r'(?P<id>[0-9]+)/update', ClientUpdateView.as_view(), name='client-update'),
    url(r'(?P<id>[0-9]+)', ClientDetailView.as_view(), name='client-detail'),
    url(r'list', ClientListView.as_view()),
    url(r'create', ClientCreateView.as_view()),
]