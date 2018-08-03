from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import CreateView, StatsPageView, HomePageView
#from entry import views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    url(r'^stats/$', StatsPageView.as_view(),name="stats"),
    url(r'^nightlystats/$', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
