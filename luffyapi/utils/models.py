from django.db import models


class BaseModel(models.Model):
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, null=True, blank=True)

    class Meta:
        # 抽象模型，一般用于设置公共模型字段的，一旦设置这个相关以后，那么dajngo在数据迁移的时候就不会为这个模型单独创建一个数据表了
        abstract = True
