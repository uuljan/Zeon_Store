from django.db import models

class Bestseller(models.Model):
    productID = models.CharField('ArticleID', max_length=50, primary_key=True)
    image = models.ImageField(upload_to ='products')
    COLOR = [
        # ('1', 'aquamarine'),
        ('2', 'lightGreen'),
        ('3', 'tan'),
        ('4', 'saddleBrown'),
        ('5', 'lavender'),
        ('6', 'white'),
        ('7', 'grey'),
        ('8', 'red'),
    ]
    color = models.CharField(max_length=20, choices=COLOR)
    title = models.CharField(max_length=50)
    price = models. IntegerField()
    price_without_discount = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=20)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title