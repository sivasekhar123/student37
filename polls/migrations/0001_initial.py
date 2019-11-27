# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-24 04:25
from __future__ import unicode_literals

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
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('M.E', 'Mechanical'), ('C.E', 'Civil'), ('E.E.E', 'Electrical'), ('E.C.E', 'Electronics'), ('C.S.E', 'Computer')], default='M.E', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StaffReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(upload_to='images')),
                ('is_staff', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentApps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('ssc', models.ImageField(upload_to='images')),
                ('inter', models.ImageField(upload_to='images')),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('father', models.CharField(max_length=30)),
                ('mother', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='images')),
                ('is_student', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Department')),
                ('student_apps', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.StudentApps')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
