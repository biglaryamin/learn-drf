from django.shortcuts import render
from blog.models import Article
from .serializer import ArticleSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser,IsAuthororReadOnly,IsSuperuserOrStaff



class ArticleList(ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsAuthororReadOnly,)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsAuthororReadOnly,)



class UserList(ListCreateAPIView):
    queryset=User.objects.all()
    # def get_queryset(self):
    #     print(reques)
    #     return super().get_queryset()
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaff,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaff,)
