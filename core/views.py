from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
