from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField('Category name', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    brend = models.BooleanField('this is a brand')
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


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='products')
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


class Blog(models.Model):
    title = models.CharField('Blog title', max_length=100)
    author = models.CharField('Auther name', max_length=100)
    img = models.ImageField('img', upload_to='media')
    text = models.TextField('text')
    created_at = models.DateTimeField(auto_now_add=True)

    def get(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'