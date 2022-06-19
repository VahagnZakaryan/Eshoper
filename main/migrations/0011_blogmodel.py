# Generated by Django 4.0.5 on 2022-06-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_product_prod_brend_category_brend'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Blog title')),
                ('author', models.CharField(max_length=100, verbose_name='Auther name')),
                ('img', models.ImageField(upload_to='media', verbose_name='img')),
                ('text', models.TextField(verbose_name='text')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
