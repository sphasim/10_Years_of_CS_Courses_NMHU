# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='semester',
            name='term_code',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='term_description',
            field=models.CharField(max_length=255),
        ),
    ]
