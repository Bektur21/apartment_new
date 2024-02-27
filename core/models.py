from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Rooms (models.Model):
    name = models.CharField(max_length = 100,default='Default Name')
    countofrooms= models.CharField(max_length = 100,verbose_name='Количество комнат')
    repair = models.TextField(verbose_name='Ремон')
    furniture = models.CharField(max_length = 50)
    square = models.IntegerField(verbose_name = 'Площадь квартиры')
    floors = models.IntegerField(verbose_name = 'Количество этажей')
    wallmaterial = models.CharField(max_length = 30,verbose_name = 'материал стен')
    heating = models.CharField(max_length = 30,verbose_name = 'Отопление')
    yearofconstraction = models.DateField(verbose_name = 'Год постройки')
    additionally =models.CharField(max_length = 20)
    district = models.ForeignKey(District,related_name='district', on_delete=models.CASCADE)
    company = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Price(models.Model):
    name = models.CharField(max_length = 100,default='Default Name')
    price = models.ForeignKey(Rooms,related_name='rooms',on_delete=models.CASCADE,verbose_name = 'Цена')
    currency = models.CharField(max_length = 20,verbose_name = 'Валюта')
    mbank = models.CharField(max_length = 20,verbose_name = 'МБанк')
    company = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"


class Market (models.Model):
    name = models.CharField(max_length = 100)
    descriptions = models.TextField(verbose_name='Описание')
    distance = models.ForeignKey(District,related_name='AREA', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Маркет"
        verbose_name_plural = "Маркеты"


class Company (models.Model):
    name = models.CharField(max_length = 30,verbose_name = 'Компания')
    history = models.TextField(verbose_name = 'История компании')
    descriptions = models.CharField(max_length = 200)
    portfolio = models.CharField(max_length = 150)
