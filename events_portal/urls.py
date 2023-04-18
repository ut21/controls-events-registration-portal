from django.urls import path
from . import views

urlpatterns = [
    #path('show_events/', views.index, name='index'),
    path('', views.add_event, name='add_event'),
]