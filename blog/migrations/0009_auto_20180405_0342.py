# Generated by Django 2.0.4 on 2018-04-05 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180405_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]