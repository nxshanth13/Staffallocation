# Generated by Django 4.1 on 2023-09-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2080)),
                ('designation', models.CharField(max_length=2080)),
                ('department', models.CharField(max_length=2080)),
                ('gender', models.CharField(max_length=2080)),
                ('subcode', models.CharField(max_length=2080)),
            ],
        ),
    ]
