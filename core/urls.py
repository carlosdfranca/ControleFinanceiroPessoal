from django.urls import path
from .views import DashboradView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', DashboradView.as_view(), name='dashboard'),
]