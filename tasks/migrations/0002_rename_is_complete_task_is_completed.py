# Generated by Django 4.0.5 on 2022-06-18 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="is_complete",
            new_name="is_completed",
        ),
    ]
