# Generated by Django 5.0.4 on 2024-04-13 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('guest', ' Guest')], max_length=10)),
            ],
        ),
    ]
