from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('', views.register_user, name='register'),
    path('coordinator_excel', views.coordinators_excel, name='coordinator_excel'),
]