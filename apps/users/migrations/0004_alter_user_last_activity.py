# Generated by Django 4.1.4 on 2023-02-11 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 30, 20, 498206, tzinfo=datetime.timezone.utc), verbose_name='last_activity'),
        ),
    ]
