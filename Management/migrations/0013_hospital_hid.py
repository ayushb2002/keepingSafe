# Generated by Django 3.1 on 2020-11-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0012_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hID',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
