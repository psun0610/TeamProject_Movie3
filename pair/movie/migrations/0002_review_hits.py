# Generated by Django 3.2.13 on 2022-09-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]