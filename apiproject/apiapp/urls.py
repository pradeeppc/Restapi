from django.conf.urls import url 
from apiapp import views 
from django.urls import path,re_path
 
urlpatterns = [ 
    url(r'^api/v2/movies/$', views.movie_list),
    url(r'^api/v2/movies/search_id/(?P<pk>[0-9]+)$', views.movie_detail),
    path('title/', views.movie_list),
    path('api/v2/movies/', views.movie_list),
] 