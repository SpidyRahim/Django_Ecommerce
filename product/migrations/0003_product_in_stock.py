# Generated by Django 4.2.7 on 2023-12-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_slug_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
