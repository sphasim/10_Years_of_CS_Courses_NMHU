# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0007_auto_20151103_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('course_number', models.PositiveIntegerField(unique=True)),
                ('term_code', models.PositiveIntegerField(unique=True)),
                ('term_description', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_type', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='offering',
            name='a_course',
        ),
    ]
