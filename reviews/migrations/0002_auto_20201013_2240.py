# Generated by Django 3.1.2 on 2020-10-13 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='jobtitle',
            new_name='job_title',
        ),
    ]
