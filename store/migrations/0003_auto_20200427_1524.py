# Generated by Django 3.0.3 on 2020-04-27 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200416_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_categoty',
            new_name='sub_category',
        ),
    ]
