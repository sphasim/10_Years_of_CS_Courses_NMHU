# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0018_delete_semester1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offering',
            old_name='max_enrollment',
            new_name='act_enrollment',
        ),
    ]
