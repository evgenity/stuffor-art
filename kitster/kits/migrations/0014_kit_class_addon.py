# Generated by Django 4.1.1 on 2022-10-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kits', '0013_kithit'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='class_addon',
            field=models.CharField(default='hero-white', max_length=200),
            preserve_default=False,
        ),
    ]
