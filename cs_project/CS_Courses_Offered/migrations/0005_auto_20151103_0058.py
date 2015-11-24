# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0004_auto_20151103_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester1',
            old_name='term_description1',
            new_name='term_description',
        ),
    ]
