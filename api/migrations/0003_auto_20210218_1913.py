# Generated by Django 3.0 on 2021-02-18 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
