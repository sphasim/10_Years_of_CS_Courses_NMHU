from django.conf.urls import patterns, include, url
from . import views

# from .views import graph, play_count_by_month

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graph', views.graph_data, name='graph_data'),
    url(r'^graph', views.graph_data,name='some_view'),
    ]