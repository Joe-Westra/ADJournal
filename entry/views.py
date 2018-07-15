from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import NightlyStatSerializer
from .models import NightlyStat

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'entry/index.html', context=None)
class StatsPageView(TemplateView):
    template_name = "stats.html"

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest API"""
    queryset = NightlyStat.objects.all()
    serializer_class = NightlyStatSerializer

    def preform_create(self, serializer):
        """Save the POST data when creating a new NightlyStat"""
        serializer.save()
