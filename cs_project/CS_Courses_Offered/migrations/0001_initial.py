# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('course_number', models.PositiveIntegerField()),
                ('course_title', models.CharField(max_length=45)),
                ('course_type', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('crn_number', models.PositiveIntegerField()),
                ('section_number', models.PositiveIntegerField()),
                ('max_enrollment', models.PositiveIntegerField()),
                ('a_course', models.ForeignKey(to='CS_Courses_Offered.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('term_code', models.PositiveIntegerField()),
                ('term_description', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='offering',
            name='a_semester',
            field=models.ForeignKey(to='CS_Courses_Offered.Semester'),
        ),
    ]
