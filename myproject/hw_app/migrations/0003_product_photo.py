# Generated by Django 5.0.3 on 2024-04-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='product_photos/'),
        ),
    ]
