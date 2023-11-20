from django.urls import path
from .views import SitterDetail, SitterList

urlpatterns = [
    path('sitters/', SitterList.as_view(), name='sitter-list'),
    path('sitters/<int:pk>', SitterDetail.as_view(), name='restaurant-detail')
  
]