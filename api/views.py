from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import TemplateView

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

# Create your views here.
