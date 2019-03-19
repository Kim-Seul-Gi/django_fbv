from django.urls import path
from . import views

app_name='boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:board_pk>/detail/', views.detail, name='detail'),
  
]
