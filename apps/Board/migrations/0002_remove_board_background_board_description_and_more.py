# Generated by Django 4.2 on 2023-04-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='background',
        ),
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
