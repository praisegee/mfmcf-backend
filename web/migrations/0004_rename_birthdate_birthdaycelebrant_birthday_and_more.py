# Generated by Django 4.2.1 on 2023-05-05 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_birthdaycelebrant_created_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='birthdaycelebrant',
            old_name='birthdate',
            new_name='birthday',
        ),
        migrations.RenameField(
            model_name='spotlight',
            old_name='birthdate',
            new_name='birthday',
        ),
    ]