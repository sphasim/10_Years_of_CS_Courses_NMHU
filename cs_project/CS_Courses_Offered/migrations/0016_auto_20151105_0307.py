# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0015_semester1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering',
            name='a_semester',
        ),
        migrations.DeleteModel(
            name='Offering',
        ),
    ]
