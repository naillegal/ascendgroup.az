# Generated by Django 4.2.2 on 2024-03-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
