from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class SaleD(models.Model):
    Gapple = models.IntegerField()
    Gorange = models.IntegerField()
    Gbowl = models.IntegerField()
    Gchopstick = models.IntegerField()
    Grag = models.IntegerField()
    Gtissue = models.IntegerField()
    Gnoddle = models.IntegerField()
    Gham = models.IntegerField()
    Gdate = models.CharField(max_length=15)

    def __str__(self):
        return self.Gdate

class ShopList(models.Model):
    ListContent = models.CharField(max_length=50)

    def __str__(self):
        return self.ListContent
