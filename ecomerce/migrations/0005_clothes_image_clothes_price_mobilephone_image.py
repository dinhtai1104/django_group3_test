# Generated by Django 4.0.2 on 2022-03-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0004_book_clothes_electronic_laptop_mobilephone_shoes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='clothes',
            name='price',
            field=models.IntegerField(default=19),
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]