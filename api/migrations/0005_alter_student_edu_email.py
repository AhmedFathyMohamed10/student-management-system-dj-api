# Generated by Django 5.0.4 on 2024-04-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_student_educational_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='edu_email',
            field=models.CharField(default='abc@mail.com', max_length=40),
        ),
    ]
