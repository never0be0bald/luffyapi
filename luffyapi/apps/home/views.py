# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Banner, Nav
from luffyapi.settings import constant
from .serializers import BannerModelSerializer, NavModelSerializer
# Create your views here.


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:constant.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class NavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False).order_by("-orders")[:constant.NAV_LENGTH]
    serializer_class = NavModelSerializer


class NavHeaderListAPIView(ListAPIView):
    queryset = Nav.objects.filter(opt=0, is_show=True, is_delete=False).order_by("orders")[:constant.NAV_LENGTH]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    queryset = Nav.objects.filter(opt=1, is_show=True, is_delete=False).order_by("orders")[:constant.NAV_LENGTH]
    serializer_class = NavModelSerializer


class Home(APIView):
    def get(self, request):
        return Response('ok')
