# Generated by Django 4.2.3 on 2023-07-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogshop',
            name='price',
            field=models.FloatField(),
        ),
    ]