# Generated by Django 4.2 on 2023-05-11 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_subject_reg_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='reg_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.registration'),
            preserve_default=False,
        ),
    ]
