# Generated by Django 4.2.2 on 2024-03-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_slider_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidecontent',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slidecontent',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slidecontent',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
