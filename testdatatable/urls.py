from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    # url(r'^$', view='myModel_asJson', name='my_ajax_url',)
    url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^table/$', login_required(TemplateView.as_view(template_name='testdatatable/albums.html'))),
    url('^api/', include(router.urls)),
    # url('^table/', index, name='albums'),
]