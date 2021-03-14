# Generated by Django 3.1.2 on 2021-03-04 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210304_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_book',
            name='author',
        ),
        migrations.AddField(
            model_name='property_book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]