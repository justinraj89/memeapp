# Generated by Django 4.1 on 2022-09-08 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_meme_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 19, 2, 24, 439995, tzinfo=datetime.timezone.utc)),
        ),
    ]