# Generated by Django 4.1.1 on 2022-09-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caches_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cache',
            name='lat',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cache',
            name='long',
            field=models.CharField(max_length=40),
        ),
    ]
