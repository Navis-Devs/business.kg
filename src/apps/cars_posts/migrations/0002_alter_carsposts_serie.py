# Generated by Django 4.2.16 on 2024-10-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsposts',
            name='serie',
            field=models.CharField(max_length=255, null=True, verbose_name='Кузов'),
        ),
    ]