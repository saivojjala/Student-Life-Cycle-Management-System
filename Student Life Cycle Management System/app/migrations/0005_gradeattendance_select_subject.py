# Generated by Django 4.2 on 2023-05-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gradeattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradeattendance',
            name='select_subject',
            field=models.CharField(choices=[("['Data Structures', 'Object Oriented Programming', 'Digital Systems Design', 'Design and Analysis of Algorithms', 'Formal Languages and Automata Theory']", "['Data Structures', 'Object Oriented Programming', 'Digital Systems Design', 'Design and Analysis of Algorithms', 'Formal Languages and Automata Theory']")], default=None, max_length=200),
            preserve_default=False,
        ),
    ]
