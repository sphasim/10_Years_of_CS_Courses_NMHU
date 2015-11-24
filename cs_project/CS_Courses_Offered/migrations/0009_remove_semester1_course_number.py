# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0008_auto_20151103_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester1',
            name='course_number',
        ),
    ]
