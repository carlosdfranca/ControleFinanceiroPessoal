from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'homepage.html'
