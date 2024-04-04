# Generated by Django 5.0.3 on 2024-04-04 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeparmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_name', models.CharField(max_length=500, verbose_name='Name')),
                ('Description', models.TextField(max_length=500, verbose_name='Desc')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=500)),
                ('stu_class', models.CharField(max_length=500)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_mobile', models.IntegerField()),
                ('stu_deparment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.deparmentmodel')),
            ],
        ),
    ]