# Generated by Django 5.1.1 on 2024-10-18 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_plane_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='bal',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plane')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plane',
            name='comments',
            field=models.ManyToManyField(related_name='plane_comments', through='main.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plane')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'plane')},
            },
        ),
        migrations.AddField(
            model_name='plane',
            name='ratings',
            field=models.ManyToManyField(related_name='plane_ratings', through='main.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
