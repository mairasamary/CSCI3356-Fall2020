# Generated by Django 3.0.2 on 2020-03-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_changed', models.DateField(default='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
