from django.db import models

class Slider(models.Model):
    img1 = models.ImageField(upload_to='carusel-img')
    img2 = models.ImageField(upload_to='carusel-img')
    img3 = models.ImageField(upload_to='carusel-img')
    img4 = models.ImageField(upload_to='carusel-img')
    img5 = models.ImageField(upload_to='carusel-img')
    main_url = models.URLField(max_length=200, blank=True)
    # def __str__(self):
    #     return self.name

class Bestseller(models.Model):
    productID = models.CharField('ArticleID', max_length=50, primary_key=True)
    image = models.ImageField(upload_to ='products')
    COLOR = [
        ('1', 'aquamarine'),
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


class Novelties(models.Model):
    NoveltiesID = models.CharField('ArticleID', max_length=50, primary_key=True)
    image_new = models.ImageField(upload_to ='products')
    COLOR = [
        ('1', 'aquamarine'),
        ('2', 'lightGreen'),
        ('3', 'tan'),
        ('4', 'saddleBrown'),
        ('5', 'lavender'),
        ('6', 'white'),
        ('7', 'grey'),
        ('8', 'red'),
    ]
    color_new = models.CharField(max_length=20, choices=COLOR)
    title_new = models.CharField(max_length=50)
    price_new = models. IntegerField()
    price_without_discount_new = models.IntegerField(null=True, blank=True)
    discount_new = models.IntegerField(null=True, blank=True)
    size_new = models.CharField(max_length=20)
    favorite_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title