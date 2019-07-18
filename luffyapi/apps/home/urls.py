from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.Home.as_view()),
    path('banner/', views.BannerListAPIView.as_view()),
    path('nav/', views.NavListAPIView.as_view()),
    path('nav/header/', views.NavHeaderListAPIView.as_view()),
    path('nav/footer/', views.NavFooterListAPIView.as_view()),
]
