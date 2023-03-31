from django.db import models

CHOICES_DISH = [
    ('P', 'Principal'),
    ('E', 'Execultivo'),
]

CHOICES_DRINK = [
    ('D', 'DESTILADOS'),
    ('A', 'ALCOOLICAS'),
    ('S', 'SEM ALCOOL'),
    ('C', 'CERVEJAS'),
]

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=1)

class Dish(Product):
    image = models.ImageField(upload_to='dish/%Y/%m/%d/', blank=True)
    preparation_time = models.CharField(max_length=30)
    serves = models.CharField(max_length=20)
    category = models.CharField(choices=CHOICES_DISH, max_length=1)

    def __str__(self):
        return f'{self.name} - {self.get_category_display()}'

class Drink(Product):
    image = models.ImageField(upload_to='drink/%Y/%m/%d/', blank=True)
    category = models.CharField(choices=CHOICES_DRINK, max_length=1)
    quantidade = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} - {self.get_category_display()}'
