# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0021_offering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering',
            name='a_course',
        ),
        migrations.RemoveField(
            model_name='offering',
            name='a_semester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_type',
        ),
        migrations.DeleteModel(
            name='Offering',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
