# Generated by Django 5.0.4 on 2024-05-04 04:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobVaccancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('numofpos', models.IntegerField(null=True)),
                ('qualification', models.CharField(default='', max_length=250)),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('experience', models.TextField(default='')),
                ('jobdesc', models.TextField(default='')),
                ('jobreq', models.TextField(default='')),
                ('Company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
