from rest_framework.serializers import ModelSerializer
from .models import Banner, Nav


class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['image', 'link']


class NavModelSerializer(ModelSerializer):
    class Meta:
        model = Nav
        fields = ['name', 'link', 'opt']
