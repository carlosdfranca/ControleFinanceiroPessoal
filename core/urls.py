from django.urls import path
from .views import DashboardView, CriarConta # Importe as views do seu app core
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', CriarConta.as_view(), name='register'),
]
