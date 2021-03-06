# Generated by Django 3.1.3 on 2020-11-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moveout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('room', models.SmallIntegerField(default=1)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('last_occupant', models.CharField(blank=True, max_length=255)),
                ('uid', models.IntegerField()),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
    ]
