# Generated by Django 3.1.2 on 2021-03-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210304_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_book',
            name='children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=0),
        ),
        migrations.AlterField(
            model_name='property_book',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
