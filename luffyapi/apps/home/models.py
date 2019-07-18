from django.db import models
from luffyapi.utils.models import BaseModel
# Create your models here.


class Banner(BaseModel):
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    note = models.CharField(max_length=150, verbose_name='备注信息')
    link = models.CharField(max_length=150, verbose_name='轮播图广告地址')
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name='是否上架', default=False)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        db_table = 'luffy_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Nav(BaseModel):
    NAV_POSITION = (
        (0, '顶部导航'),
        (1, '底部导航')
    )
    name = models.CharField(max_length=50, verbose_name='导航名称')
    link = models.CharField(max_length=250, verbose_name='导航地址')
    opt = models.SmallIntegerField(choices=NAV_POSITION, default=0, verbose_name='位置')

    class Meta:
        db_table = 'luffy_nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
