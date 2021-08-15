from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Article
from .serializer import ArticleSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
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
    #     print(self.request.user)
    #     print(self.request.auth)
    #     print("---------------------")
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaff,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaff,)


class RevokeToken(APIView):
    permission_classes=(IsAuthenticated,)

    def delete(self,request):
        request.auth.delete()
        return Response(status=204)
