from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import CreateView
from entry import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homer'),
    url(r'^stats/$', views.StatsPageView.as_view()),
    url(r'^nightlystats/$', CreateView.as_view(), name="create"),
#    url(r'^', views.HomePageView.as_view()),

]

#urlpatterns = format_suffix_patterns(urlpatterns)
