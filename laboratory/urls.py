from django.urls import path

from laboratory import views

urlpatterns = [
    path('', views.index,name='index'),
    path('team/', views.team,name='team'),
]