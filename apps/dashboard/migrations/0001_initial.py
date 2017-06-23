# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('mess_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='login.User')),
                ('mess_wall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wall_messages', to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comm_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dashboard.Message'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comm_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login.User'),
        ),
    ]