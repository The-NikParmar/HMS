# Generated by Django 4.2.15 on 2024-08-30 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patient", "0001_initial"),
        ("custom_admin", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="disease",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="custom_admin.disease"
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
