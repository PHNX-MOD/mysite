# Generated by Django 3.0.3 on 2020-05-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200513_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
