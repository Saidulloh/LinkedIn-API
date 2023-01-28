# Generated by Django 4.1.4 on 2023-01-28 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_likes', to=settings.AUTH_USER_MODEL, verbose_name='owner_likes')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_likes', to='posts.post', verbose_name='posts_likes')),
            ],
            options={
                'verbose_name': 'Post like',
                'verbose_name_plural': 'Posts likes',
            },
        ),
    ]
