# Generated by Django 3.0.5 on 2021-03-29 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_auto_20210329_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tests',
            name='test_status',
        ),
    ]
