# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-03 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('ip', models.CharField(max_length=30)),
                ('cname', models.CharField(max_length=45)),
                ('idc_id', models.IntegerField()),
                ('role', models.CharField(max_length=10)),
                ('rack', models.CharField(max_length=30)),
                ('assert_num', models.CharField(max_length=30)),
                ('u_phone', models.IntegerField()),
                ('u_id', models.IntegerField()),
                ('update_time', models.IntegerField()),
                ('rep_info', models.CharField(max_length=45)),
                ('post_time', models.IntegerField()),
                ('status', models.IntegerField(default='0')),
                ('modelNum', models.CharField(default='0000-0000', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=30)),
                ('isp', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('update_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Isp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maintance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('msg', models.CharField(max_length=300)),
                ('ip', models.CharField(max_length=30)),
                ('idc_id', models.IntegerField()),
                ('update_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='saltTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('cmd', models.CharField(max_length=100)),
                ('u_id', models.IntegerField()),
                ('host_id', models.IntegerField()),
                ('update_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('pwd', models.CharField(max_length=45)),
            ],
        ),
    ]
