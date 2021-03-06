# Generated by Django 3.2 on 2021-10-09 09:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211008_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contact_number',
            field=phone_field.models.PhoneField(blank=True, default=None, help_text='Contact phone number', max_length=31),
        ),
    ]
