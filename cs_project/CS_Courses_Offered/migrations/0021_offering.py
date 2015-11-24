# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0020_auto_20151111_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn_number', models.PositiveIntegerField()),
                ('section_number', models.PositiveIntegerField()),
                ('max_enrollment', models.PositiveIntegerField()),
                ('act_enrollment', models.PositiveIntegerField()),
                ('a_course', models.ForeignKey(to='CS_Courses_Offered.Course')),
                ('a_semester', models.ForeignKey(to='CS_Courses_Offered.Semester')),
            ],
        ),
    ]
