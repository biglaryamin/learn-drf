from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import RevokeToken




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    path('api/token-auth/', obtain_auth_token),
    path('api/revoke/', RevokeToken.as_view()),
    
]
