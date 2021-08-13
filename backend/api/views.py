from django.shortcuts import render
from blog.models import Article
from .serializer import ArticleSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser


class ArticleList(ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer




class UserList(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsAdminUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsAdminUser,)
