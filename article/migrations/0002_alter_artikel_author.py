# Generated by Django 4.1 on 2022-12-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]