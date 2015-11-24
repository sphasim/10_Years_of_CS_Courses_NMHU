# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0012_delete_semester1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester1',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('term_code1', models.PositiveIntegerField(unique=True)),
                ('term_description', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_type', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
    ]
