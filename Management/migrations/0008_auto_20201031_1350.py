# Generated by Django 3.1 on 2020-10-31 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0007_data_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': 'Data'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Location'},
        ),
    ]
