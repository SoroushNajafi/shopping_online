# Generated by Django 4.1.1 on 2022-09-28 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
