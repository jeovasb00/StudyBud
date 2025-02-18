# Generated by Django 4.2.19 on 2025-02-18 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
