# Generated by Django 3.2 on 2021-10-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211008_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='education',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]