from django.shortcuts import render

# Create your views here.
# frontend/views.py

from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = 'index.html'
