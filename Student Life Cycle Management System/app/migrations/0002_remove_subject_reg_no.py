# Generated by Django 4.2 on 2023-05-11 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='reg_no',
        ),
    ]
