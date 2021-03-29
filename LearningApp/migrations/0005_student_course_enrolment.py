# Generated by Django 3.0.5 on 2021-03-29 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0004_auto_20210329_1007'),
        ('LearningApp', '0004_auto_20210329_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_course_enrolment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entrollment', models.DateField()),
                ('date_of_completion', models.DateField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseApp.Courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningApp.Students')),
            ],
        ),
    ]
