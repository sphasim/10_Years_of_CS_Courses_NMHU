# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0022_auto_20151208_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('crn_number', models.PositiveIntegerField()),
                ('course_type', models.CharField(max_length=255)),
                ('section_number', models.PositiveIntegerField()),
                ('max_enrollment', models.PositiveIntegerField()),
                ('act_enrollment', models.PositiveIntegerField()),
                ('a_course', models.ForeignKey(to='CS_Courses_Offered.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('term_code', models.PositiveIntegerField(unique=True)),
                ('term_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='offering',
            name='a_semester',
            field=models.ForeignKey(to='CS_Courses_Offered.Semester'),
        ),
    ]
