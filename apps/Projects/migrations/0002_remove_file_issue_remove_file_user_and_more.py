# Generated by Django 4.2 on 2023-04-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
