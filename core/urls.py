from django.urls import path
from .views import HomepageView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
]