
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^api/auth/jwt/$', obtain_jwt_token), 
    url(r'^', include('apiapp.urls')), 
]
