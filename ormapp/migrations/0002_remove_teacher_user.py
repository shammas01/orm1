# Generated by Django 4.2.3 on 2023-08-10 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]
