# Generated by Django 5.1.4 on 2024-12-25 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=32)),
                ('date_naissance', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('tlf', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=302)),
                ('Amis', models.ManyToManyField(blank=True, to='Monface.person')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monface.faculty')),
            ],
        ),
    ]
