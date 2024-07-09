from django.contrib.sites import requests
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from serializers import PoetSerializers
from .models import Person, Category


class CRUDPoet(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
      # queryset = Person.objects.all() #buni oldiga [:3] beromimiz, chunki bu как SQL so'rovidek, boradi hamma ma'lumotlarni olib keladi
      serializer_class = PoetSerializers
      def get_queryset(self):
          return Person.objects.all()#[:3]


      @action(methods=["get"], detail=False)
      def category(self, request):
          cats = Category.objects.all()
          return Response({"cats": [x.name for x in cats]})




# class ListCreatePoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
#
#
# class UpdateDeleteRetrivePoet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers




# class ListPoet(APIView):
#     def get(self, request, pk):
#         if not pk:
#             return Response({"post": "Метод GET не создан"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#
#         except:
#             return Response({"post": "Объект не найден!"})
#         serializers = PoetSerializers(instance)
#         return Response({"post": serializers.data})
#
# class CreatePoet(APIView):
#     def post(self, requests):
#         serializers = PoetSerializers(data=requests.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#
#         return Response({"posts": serializers.data})
#
#
#
# class UpdateDeletePoet(APIView):
#     def put(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Метод PUT не создан"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.save()
#
#         except:
#             return Response({"post": "Объект не найден!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#
#     def patch(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Метод PATCH не создан"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.save()
#
#         except:
#             return Response({"post": "Объект не найден!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Метод DELETE не создан"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.save()
#             instance.delete()
#         except:
#             return Response({"post": "Объект не найден!"})
#
#         return Response({"answer": f"deleted '{pk}' id"})