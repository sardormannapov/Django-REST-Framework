from django.contrib.sites import requests
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import PoetSerializers
from .models import Person

class ListPoet(APIView):
    def get(self, requests):
        lst = Person.objects.all().values()
        return Response({"Поэт": list(lst)})

    def post(self, requests):
        serializers = PoetSerializers(data=requests.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({"posts": serializers.data})

    def put(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Метод PUT не создан"})

        try:
            instance = Person.objects.get(pk=pk)
            instance.save()

        except:
            return Response({"post": "Объект не найден!"})

        serializers = PoetSerializers(data=requests.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})


    def patch(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Метод PATCH не создан"})

        try:
            instance = Person.objects.get(pk=pk)
            instance.save()

        except:
            return Response({"post": "Объект не найден!"})

        serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})


    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Метод DELETE не создан"})

        try:
            instance = Person.objects.get(pk=pk)
            instance.save()
            instance.delete()
        except:
            return Response({"post": "Объект не найден!"})

        return Response({"answer": f"deleted '{pk}' id"})