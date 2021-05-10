from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConsumerSerializer
from .models import Consumer


class ConsumerViewset(viewsets.ModelViewSet):
    queryset = Consumer.objects.all().order_by('name')
    serializer_class = ConsumerSerializer

# Create your views here.
