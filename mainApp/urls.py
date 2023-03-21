from django.urls import path
from mainApp import views

urlpatterns = [
    path('', views.index,name="index"),
    path('use/', views.use,name="use"),
]
