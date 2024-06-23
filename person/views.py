from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from serializers import PoetSerializers
from .models import Person

class ListPoet(APIView):
    def get(self, request):
        lst = Person.objects.all().values()
        return Response({"Поэт": list(lst)})

    def post(self, request):
        posts = Person.objects.create(
            name=request.data["name"],
            content=request.data["content"],
            cat_id=request.data["cat_id"],
        )
        return Response({"posts": model_to_dict(posts)})



