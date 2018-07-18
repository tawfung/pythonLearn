from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Album, Artist
from .serializers import AlbumSerializer, ArtistSerializer

from django.contrib.auth import authenticate, logout, login
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

def index(request):
    return render(request, 'testdatatable/albums.html')


class LoginView(TemplateView):
    template_name = 'backoffice/index.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)
class LogoutView(TemplateView):
    template_name = 'backoffice/index.html'
    def get(self, request, **kwargs):
        login(request)
        return render(request, self.template_name)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('rank')
    serializer_class = AlbumSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

class ArtistViewSet(viewsets.ViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)