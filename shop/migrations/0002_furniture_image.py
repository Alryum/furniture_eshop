# Generated by Django 4.1.7 on 2023-03-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='image',
            field=models.ImageField(default=None, upload_to='products_images/'),
            preserve_default=False,
        ),
    ]