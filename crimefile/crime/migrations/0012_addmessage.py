# Generated by Django 2.1.5 on 2019-04-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0011_addcrime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addmessage',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=100)),
                ('msg', models.TextField(max_length=500)),
                ('rpy', models.TextField(max_length=500)),
            ],
        ),
    ]