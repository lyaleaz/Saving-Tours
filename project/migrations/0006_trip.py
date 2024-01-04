# Generated by Django 4.0.3 on 2022-05-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('To', models.CharField(default='', max_length=100)),
                ('From', models.CharField(default='', max_length=100)),
                ('BusLine', models.CharField(default='', max_length=100)),
                ('DateTime', models.DateTimeField()),
            ],
            options={
                'db_table': 'Trips',
            },
        ),
    ]