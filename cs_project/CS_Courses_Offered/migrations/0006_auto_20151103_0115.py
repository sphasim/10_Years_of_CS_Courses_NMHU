# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0005_auto_20151103_0058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Semester1',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='term_code',
            new_name='course_number',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='term_description',
            new_name='course_title',
        ),
    ]
