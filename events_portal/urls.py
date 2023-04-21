from django.urls import path
from . import views

urlpatterns = [
    #path('show_events/', views.index, name='index'),
    path('', views.add_event, name='add_event'),
    path('show_events/', views.show_events, name='show_events'),
    path('events_csv/', views.event_csv, name='event_csv'),
    path('events_excel/', views.events_excel, name='event_excel'),
]