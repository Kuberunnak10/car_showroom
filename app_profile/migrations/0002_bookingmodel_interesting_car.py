# Generated by Django 5.0.1 on 2024-02-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingmodel",
            name="interesting_car",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]