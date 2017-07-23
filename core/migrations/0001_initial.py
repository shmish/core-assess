# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigIdeaRubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeLevel', models.IntegerField(choices=[(8, '8'), (9, '9')], default=8)),
                ('courseName', models.CharField(choices=[('MA', 'Mathematics'), ('AR', 'Arts Eduction'), ('EN', 'English Language Arts'), ('SC', 'Science'), ('SS', 'Social Studies')], max_length=2)),
                ('bigIdea', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CoreComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iCan', models.CharField(max_length=100)),
                ('core_comp', models.CharField(choices=[('CT', 'Critical Thinking'), ('CR', 'Creative Thinking'), ('SR', 'Social Responsibility'), ('CO', 'Communication'), ('PA', 'Personal Awareness'), ('CI', 'Cultural Identity')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('artifact', models.CharField(max_length=200)),
                ('signif', models.CharField(max_length=200)),
                ('dateAdded', models.DateTimeField(blank=True, verbose_name='date added')),
                ('corecomp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CoreComp')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddy', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('SIN', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='evidence',
            name='studentname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
    ]
