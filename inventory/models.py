from django.db import models

from piro import settings


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    photo = models.ImageField(blank=True, verbose_name='제품 사진', upload_to='image')
    desc = models.TextField(blank=True, verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    amount = models.PositiveIntegerField(verbose_name='남은 수량')


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='제목')
    tel = models.CharField(max_length=200, verbose_name='전화번호')
    address = models.CharField(max_length=200, verbose_name='주소')


def get_image_url(self):
    return '%s%s' % (settings.MEDIA_URL, self.image)
