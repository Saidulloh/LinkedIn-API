# Generated by Django 4.1.4 on 2023-01-28 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 19, 8, 54, 939523, tzinfo=datetime.timezone.utc), verbose_name='last_activity'),
        ),
    ]
