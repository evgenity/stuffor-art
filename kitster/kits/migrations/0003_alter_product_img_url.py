# Generated by Django 4.1.1 on 2022-10-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kits', '0002_rename_product_description_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.FileField(upload_to=''),
        ),
    ]