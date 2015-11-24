# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0002_auto_20151102_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester1',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('term_code1', models.PositiveIntegerField(unique=True)),
                ('term_description1', models.CharField(max_length=255)),
            ],
        ),
    ]
