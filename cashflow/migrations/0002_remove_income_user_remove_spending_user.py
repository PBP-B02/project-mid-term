# Generated by Django 4.1 on 2022-12-11 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='user',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='user',
        ),
    ]