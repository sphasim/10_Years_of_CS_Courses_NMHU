# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0006_auto_20151103_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='course_number',
            new_name='term_code',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='course_title',
            new_name='term_description',
        ),
    ]
