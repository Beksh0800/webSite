from django.db import models


class Sushi(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Description")
    image = models.CharField("Ссылка на фото", max_length=200)
    price = models.IntegerField("Price")
    count = models.IntegerField("Количество")

    def __str__(self):
        return self.name


class Sets(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.CharField("Ссылка на фото", max_length=200)
    price = models.IntegerField("Price")
    count = models.IntegerField("Количество")

    def __str__(self):
        return self.name
