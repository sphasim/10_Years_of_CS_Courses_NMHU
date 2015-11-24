# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0009_remove_semester1_course_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Semester1',
        ),
    ]
