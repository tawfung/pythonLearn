"""django_angular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet
# from django_angular.views import IndexView
from authentication.views import LoginView
 
router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login', LoginView.as_view(), name='login'),
    # url(r'^register/', include(router.urls)),
    # url(r'^.*$', IndexView.as_view(), name='index'),
    ]

