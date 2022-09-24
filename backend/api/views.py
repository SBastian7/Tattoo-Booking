from django.shortcuts import render

# Create your views here.
from .models import Brand
from .serializers import BrandSerializer

from rest_framework import viewsets

class BrandViewset(viewsets.ModelViewSet):  
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
