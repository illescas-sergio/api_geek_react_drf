# Generated by Django 4.2.4 on 2023-08-21 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_drf', '0003_product_sectionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sectionId',
        ),
    ]
