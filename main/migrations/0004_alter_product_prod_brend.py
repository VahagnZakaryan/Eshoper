# Generated by Django 4.0.5 on 2022-06-16 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_brend_product_prod_brend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_brend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brends', to='main.brend'),
        ),
    ]
