# Generated by Django 3.1 on 2020-11-03 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Management', '0010_auto_20201031_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Hospital',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=32)),
                ('last', models.CharField(max_length=32)),
                ('organization', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Volunteer',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing1', models.CharField(max_length=15)),
                ('max_appointments1', models.IntegerField()),
                ('timing2', models.CharField(max_length=15, null=True)),
                ('max_appointments2', models.IntegerField(null=True)),
                ('timing3', models.CharField(max_length=15, null=True)),
                ('max_appointments3', models.IntegerField(null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=64)),
                ('spec', models.CharField(max_length=64)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.hospital')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.slot')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.doctor')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.slot')),
            ],
        ),
    ]
