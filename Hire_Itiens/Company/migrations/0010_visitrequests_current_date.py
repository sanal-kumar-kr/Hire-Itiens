# Generated by Django 5.0.4 on 2024-05-08 08:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0009_visitrequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitrequests',
            name='current_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
