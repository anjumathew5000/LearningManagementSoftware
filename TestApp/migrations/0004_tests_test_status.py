# Generated by Django 3.0.5 on 2021-03-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0003_remove_tests_test_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='test_status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
