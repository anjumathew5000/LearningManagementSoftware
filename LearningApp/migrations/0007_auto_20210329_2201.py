# Generated by Django 3.0.5 on 2021-03-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningApp', '0006_student_course_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_course_enrolment',
            name='date_of_completion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
