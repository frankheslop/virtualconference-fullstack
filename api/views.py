from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = 'index.html'

# Create your views here.
