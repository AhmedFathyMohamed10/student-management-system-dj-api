# Generated by Django 5.0.4 on 2024-04-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_student_edu_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='edu_email',
        ),
    ]
