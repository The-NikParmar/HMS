# Generated by Django 5.1 on 2024-09-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_appointment_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
