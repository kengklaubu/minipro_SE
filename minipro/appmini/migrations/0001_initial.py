# Generated by Django 5.0.6 on 2024-12-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_name", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField()),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
