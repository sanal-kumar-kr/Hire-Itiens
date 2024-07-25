# Generated by Django 5.0.4 on 2024-05-10 04:20

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
            name='visitrequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('cv', models.FileField(null=True, upload_to='')),
                ('Company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cvc', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcv', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
