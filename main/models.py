from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField('Category name', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='url')

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brend(models.Model):
    title = models.CharField('Brend name', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brend'
        verbose_name_plural = 'Brends'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='products')
    prod_brend = models.ForeignKey(Brend, on_delete=models.CASCADE, related_name='brends', null=True)
    name = models.CharField('Product name', max_length=100)
    description = models.TextField('product description')
    img = models.ImageField(upload_to='media')
    web_id = models.IntegerField('Web ID')
    price = models.IntegerField('price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Slider(models.Model):
    title = models.CharField('slider title', max_length=100)
    slogan = models.TextField('slogan')
    comment = models.TextField('comment')
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'