# Generated by Django 5.0.2 on 2024-03-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_register_company_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='college_certificate',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='register',
            name='college_desc',
            field=models.TextField(null=True),
        ),
    ]
