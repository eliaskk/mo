# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseaseName', models.CharField(max_length=500, verbose_name='\u75c5\u540d')),
                ('patientContent', models.CharField(max_length=500, verbose_name='\u60a3\u8005')),
                ('contentVec', models.CharField(max_length=500, null=True)),
                ('prescriptionName', models.CharField(max_length=500, verbose_name='\u5f00\u65b9\u540d')),
                ('prescriptions', models.CharField(max_length=500, verbose_name='\u5f00\u65b9')),
                ('prescriptionsReasons', models.CharField(max_length=500, null=True, verbose_name='\u5f00\u65b9\u539f\u56e0')),
                ('sourceFrom', models.CharField(default='\u80e1\u5e0c\u6055\u4f24\u5bd2\u65b9\u8bc1\u8fa9\u8bc1', max_length=500, verbose_name='\u6765\u6e90')),
            ],
        ),
    ]