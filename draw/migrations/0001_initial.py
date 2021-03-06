# Generated by Django 2.0 on 2018-03-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('station', models.IntegerField()),
                ('fre', models.DecimalField(decimal_places=2, max_digits=14)),
                ('app_time', models.DateTimeField()),
                ('disapp_time', models.DateTimeField()),
                ('back_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flag', models.IntegerField()),
            ],
            options={
                'db_table': 'test',
            },
        ),
    ]
