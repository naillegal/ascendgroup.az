# Generated by Django 5.0.3 on 2024-03-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
