# Generated by Django 4.2.2 on 2023-07-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_forms', '0002_feedback_rename_new_user_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(max_length=500),
        ),
    ]
