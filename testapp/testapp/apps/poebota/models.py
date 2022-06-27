from django.db import models


# Создаём модель своего приложения для базы данных
# Create your models here.

class Tovar(models.Model):
    tovar_name = models.CharField('Название', max_length=50)
    tovar_price = models.FloatField('Цена', max_length=50)
    def __str__(self):
        return self.tovar_name

