# Generated by Django 4.1.1 on 2022-09-28 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_product_categories_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('women', 'women'), ('men', 'men'), ('kids', 'kids'), ('extra', 'accessories')], max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(blank=True, choices=[('women', 'women'), ('men', 'men'), ('kids', 'kids'), ('extra', 'accessories')], max_length=200),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
    ]