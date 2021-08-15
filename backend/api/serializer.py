from django.db.models import fields
from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model  =Article
        # fields=('title','slug','author','content','publish','status')
        # exclude=('created','updated')
        fields="__all__"

        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  =User
        fields="__all__"

    




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']
        

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user



