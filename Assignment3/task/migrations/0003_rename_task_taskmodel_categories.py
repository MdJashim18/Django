# Generated by Django 4.2.16 on 2024-11-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_taskmodel_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='task',
            new_name='categories',
        ),
    ]