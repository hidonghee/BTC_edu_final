# Generated by Django 4.1.3 on 2022-11-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('sex', models.CharField(max_length=10)),
                ('addr', models.CharField(max_length=300)),
                ('register_dttm', models.DateTimeField(auto_now_add=True)),
                ('access_key', models.CharField(max_length=200, null=True, unique=True)),
                ('secret_key', models.CharField(max_length=200, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
    ]
