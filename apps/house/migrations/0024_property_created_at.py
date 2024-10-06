# Generated by Django 5.1.1 on 2024-10-06 14:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0023_alter_residentialcategory_housing_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]