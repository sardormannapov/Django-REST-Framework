from django.shortcuts import render
from rest_framework import generics

from serializers import PoetSerializers
from .models import Person
class ListPoet(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PoetSerializers


