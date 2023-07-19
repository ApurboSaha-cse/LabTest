from django.shortcuts import render
from rest_framework import generics
from .models import DogShop
from .serializers import DogShopSerializer

# Create your views here.
class DogList(generics.ListCreateAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogShopSerializer

class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogShopSerializer

