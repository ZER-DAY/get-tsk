# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

# Generated by Django 1.9.2 on 2016-09-01 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0002_epic_color'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relateduserstory',
            unique_together=set([('user_story', 'epic')]),
        ),
    ]
