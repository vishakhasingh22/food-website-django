# Generated by Django 4.2 on 2024-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(default=0),
        ),
    ]