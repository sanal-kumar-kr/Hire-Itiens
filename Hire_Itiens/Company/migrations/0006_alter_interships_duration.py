# Generated by Django 5.0.4 on 2024-05-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0005_alter_jobvaccancies_interviewtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interships',
            name='duration',
            field=models.CharField(default='', max_length=250),
        ),
    ]
