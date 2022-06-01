from django.db import models
from colorfield.fields import ColorField

class Slider(models.Model):
    img1 = models.ImageField(upload_to='carusel-img')
    img2 = models.ImageField(upload_to='carusel-img')
    img3 = models.ImageField(upload_to='carusel-img')
    img4 = models.ImageField(upload_to='carusel-img')
    img5 = models.ImageField(upload_to='carusel-img')
    main_url = models.URLField(max_length=200, blank=True)
    # def __str__(self):
    #     return self.name

class Collection(models.Model):
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image_collection = models.ImageField(upload_to='products', default="nno")
    name = models.CharField(max_length=200, db_index=True)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Bestseller(models.Model):
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200, db_index=True)
    # productID = models.CharField('ArticleID', max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    price = models. IntegerField()
    price_with_discount = models.IntegerField(blank=True)
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)
    size = models.CharField(max_length=20)
    favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products')
    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        '''Расчитать стоимость со скидкой'''
        self.price_with_discount = int(self.price * (100 - self.discount) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ImageBestseller(models.Model):
    image = models.ImageField(upload_to='products')
    COLOR_PALETTE = [
        ('#BED5D2', '#BED5D2'),
        ('#D6EEC4', '#D6EEC4'),
        ('#002B73', '#002B73'),
        ('#AC8549', '#AC8549'),
        ('#BAC0F8', '#BAC0F8'),
        ('#FDFDFD', '#FDFDFD'),
        ('#D3D3D2', '#D3D3D2'),
        ('#FF8888', '#FF8888'),
    ]
    color = ColorField(choices=COLOR_PALETTE, default='#FF0000')
    bestseller = models.ForeignKey('Bestseller', related_name='images', on_delete=models.CASCADE)

class Noveltie(models.Model):
    # NoveltiesID = models.CharField('ArticleID', max_length=50, primary_key=True)
    image_new = models.ImageField(upload_to ='products')
    title_new = models.CharField(max_length=50)
    price_new = models. IntegerField()
    price_with_discount_new = models.IntegerField(blank=True)
    discount_new = models.IntegerField('Скидка в процентах', blank=True, default=0)
    size_new = models.CharField(max_length=20)
    favorite_new = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        '''Расчитать стоимость со скидкой'''
        self.price_with_discount_new = int(self.price_new * (100 - self.discount_new) / 100)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title_new

class ImageNoveltie(models.Model):
    image = models.ImageField(upload_to='products')
    COLOR_PALETTE = [
        ('#BED5D2', '#BED5D2'),
        ('#D6EEC4', '#D6EEC4'),
        ('#002B73', '#002B73'),
        ('#AC8549', '#AC8549'),
        ('#BAC0F8', '#BAC0F8'),
        ('#FDFDFD', '#FDFDFD'),
        ('#D3D3D2', '#D3D3D2'),
        ('#FF8888', '#FF8888'),
    ]
    color = ColorField(choices=COLOR_PALETTE, default='#FF0000')
    noveltie = models.ForeignKey('Noveltie', related_name='images_new', on_delete=models.CASCADE)



class Advantage(models.Model):
    image = models.ImageField(upload_to='products')
    title_advantage = models.CharField(max_length=150)
    description_advantage = models.TextField()

    def __str__(self):
        return self.title_advantage
