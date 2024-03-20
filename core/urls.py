from django.urls import path
from core.views import DashboardView # Importe as views do seu app core

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]
