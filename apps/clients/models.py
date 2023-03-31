from django.db import models
from django.contrib.auth.models import User
from core.models import Product

class Client(User):
    rg = models.CharField(max_length=11, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    image = models.ImageField(upload_to='clients/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateField(default='', blank=True)

    def __str__(self):
        return self.get_full_name()

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.client.first_name} - {self.product} - {self.amount}'

