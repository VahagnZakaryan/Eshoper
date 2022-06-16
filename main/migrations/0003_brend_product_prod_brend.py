# Generated by Django 4.0.5 on 2022-06-16 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_category_parent_category_slug_delete_firm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Brend name')),
            ],
            options={
                'verbose_name': 'Brend',
                'verbose_name_plural': 'Brends',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='prod_brend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brend', to='main.brend'),
        ),
    ]
