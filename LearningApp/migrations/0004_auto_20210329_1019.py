# Generated by Django 3.0.5 on 2021-03-29 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearningApp', '0003_courses_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tests',
            name='Course_id',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Tests',
        ),
    ]
