# Generated by Django 5.0.1 on 2024-02-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_autosalon", "0003_alter_mark_car_image_galery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mark",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
