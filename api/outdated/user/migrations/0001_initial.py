# Generated by Django 4.1.9 on 2023-06-08 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("idp_id", models.CharField(max_length=255, null=True, unique=True)),
                ("first_name", models.CharField(max_length=150, null=True)),
                ("last_name", models.CharField(max_length=150, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=255, null=True, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
