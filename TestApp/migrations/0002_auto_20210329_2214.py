# Generated by Django 3.0.5 on 2021-03-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tests',
            name='test_totalmark',
        ),
        migrations.AddField(
            model_name='tests',
            name='test_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
