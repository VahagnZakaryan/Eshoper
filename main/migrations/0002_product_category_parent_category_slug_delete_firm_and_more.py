# Generated by Django 4.0.5 on 2022-06-16 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('description', models.TextField(verbose_name='product description')),
                ('img', models.ImageField(upload_to='media')),
                ('web_id', models.IntegerField(verbose_name='Web ID')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='main.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=100, unique=True, verbose_name='url'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Firm',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category'),
        ),
    ]