# Generated by Django 4.1.1 on 2023-02-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_authority',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
