# Generated by Django 4.1 on 2022-12-11 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_artikel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikel',
            name='author',
        ),
    ]