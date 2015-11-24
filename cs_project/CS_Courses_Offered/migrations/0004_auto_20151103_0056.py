# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0003_semester1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester1',
            old_name='term_code1',
            new_name='term_code',
        ),
    ]
