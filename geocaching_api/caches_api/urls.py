from django.urls import path
from . import views

urlpatterns = [
    path('api/caches', views.CacheList.as_view(), name='cache_list'),
    path('api/caches/<int:pk>', views.CacheDetail.as_view(), name='cache_detail'),
]