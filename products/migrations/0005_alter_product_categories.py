# Generated by Django 4.1.1 on 2022-09-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(blank=True, choices=[('women', 'women'), ('men', 'men'), ('kid', 'kid')], max_length=200),
        ),
    ]