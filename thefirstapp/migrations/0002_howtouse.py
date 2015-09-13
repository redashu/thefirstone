# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thefirstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Howtouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step_title', models.CharField(max_length=255)),
                ('step1', models.TextField()),
                ('step2', models.TextField()),
                ('step3', models.TextField()),
                ('app_name', models.ForeignKey(to='thefirstapp.Appnames')),
            ],
        ),
    ]
