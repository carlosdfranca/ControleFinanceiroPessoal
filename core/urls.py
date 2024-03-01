from django.urls import path
from .views import HomepageView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]