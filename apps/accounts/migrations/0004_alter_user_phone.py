# Generated by Django 5.1.1 on 2024-10-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_last_name_user_phone_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Phone'),
        ),
    ]