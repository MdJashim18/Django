# Generated by Django 4.2.16 on 2024-11-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]