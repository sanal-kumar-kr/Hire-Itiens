# Generated by Django 5.0.4 on 2024-05-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobvaccancies',
            name='interviewdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='jobvaccancies',
            name='interviewtime',
            field=models.DateTimeField(null=True),
        ),
    ]
