# Generated by Django 5.0.4 on 2024-05-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_jobvaccancies_interviewdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='interships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('desc', models.TextField(default='')),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
    ]
