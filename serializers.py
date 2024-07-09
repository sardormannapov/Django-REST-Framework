from rest_framework import serializers
from rest_framework.response import Response

from person.models import Person
from person.models import Category


class PoetSerializers(serializers.ModelSerializer):
        class Meta:   #Har doim Meta yozishimiz shart, chunki bu baza
            model = Person
            fields = ("id", "name", "content")



        # name = serializers.CharField(max_length=250)
        # content = serializers.CharField()
        # time_create = serializers.DateTimeField(read_only=True) #read_only=True - bu поле обязательно emas degani
        # time_update = serializers.DateTimeField(read_only=True)
        # is_published = serializers.BooleanField(default=True)
        # cat_id = serializers.IntegerField()
        #
        #
        # def create(self, validated_data): #validated_data - bu biz bervorotgan ma'lumot
        #         return Person.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #         instance.name = validated_data.get("name", instance.name)
        #         instance.content = validated_data.get("content", instance.content)
        #         instance.time_update = validated_data.get("time_update", instance.time_update)
        #         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        #         instance.save()
        #         return instance


