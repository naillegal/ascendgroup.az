# Generated by Django 4.2.2 on 2024-03-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_laminate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
