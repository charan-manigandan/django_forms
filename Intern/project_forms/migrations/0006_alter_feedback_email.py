# Generated by Django 4.2.2 on 2023-07-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_forms', '0005_alter_feedback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
