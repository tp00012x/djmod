# Generated by Django 2.0.4 on 2018-04-05 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180405_0330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='field',
            new_name='title',
        ),
    ]