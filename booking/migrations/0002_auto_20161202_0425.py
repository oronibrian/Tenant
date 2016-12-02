# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='Gender', choices=[(b'males', 'Females'), (b'male', 'female')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='title',
            field=models.CharField(blank=True, max_length=10, verbose_name='Title', choices=[(b'mr', 'Mr.'), (b'mrs', 'Mrs.'), (b'dr', 'Dr.'), (b'prof', 'Prof.')]),
        ),
    ]
