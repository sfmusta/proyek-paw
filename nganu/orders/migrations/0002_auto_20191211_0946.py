# Generated by Django 3.0 on 2019-12-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattertype',
            name='large_price',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='plattertype',
            name='small_price',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]
