# Generated by Django 5.0.4 on 2024-05-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_ropa_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='image_url',
            field=models.CharField(max_length=2083),
        ),
    ]
