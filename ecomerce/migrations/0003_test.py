# Generated by Django 4.0.2 on 2022-03-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]