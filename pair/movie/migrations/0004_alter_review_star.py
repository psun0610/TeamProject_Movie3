# Generated by Django 3.2.13 on 2022-09-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_review_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.CharField(default='⭐⭐⭐⭐⭐', max_length=10),
        ),
    ]
