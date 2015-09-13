# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thefirstapp', '0002_howtouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='howtouse',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
