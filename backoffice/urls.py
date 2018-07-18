from django.conf.urls import url
from rest_framework import routers
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^table/$', login_required(TemplateView.as_view(template_name='testdatatable/albums.html'))),
]