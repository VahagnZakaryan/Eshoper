# Generated by Django 4.0.5 on 2022-06-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_slogan_brend_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_brend',
            field=models.BooleanField(default=0, verbose_name='this is a brand'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Brend',
        ),
    ]
