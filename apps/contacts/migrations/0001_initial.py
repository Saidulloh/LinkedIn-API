# Generated by Django 4.1.4 on 2023-02-03 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_owner', to=settings.AUTH_USER_MODEL, verbose_name='contact_owner')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
