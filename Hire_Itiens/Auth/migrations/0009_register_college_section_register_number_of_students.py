# Generated by Django 5.0.4 on 2024-05-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_alter_register_mnc_alter_register_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='college_section',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='number_of_students',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
