# Generated by Django 2.0.4 on 2018-04-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180405_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
