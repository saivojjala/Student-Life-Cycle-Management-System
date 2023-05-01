# Generated by Django 4.2 on 2023-05-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slcm', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('reg_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
