from django.shortcuts import render

# Create your views here.
from rest_framework import generics 
from .serializers import CacheSerializer
from .models import Cache 

# /caches POST + GET ROUTES
class CacheList(generics.ListCreateAPIView):
    queryset = Cache.objects.all().order_by('id')
    serializer_class = CacheSerializer

# /caches/:id
class CacheDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cache.objects.all().order_by('id')
    serializer_class = CacheSerializer