# Generated by Django 5.1.6 on 2025-03-04 08:20

import datetime
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
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
                (
                    "uuid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet=None, length=10, max_length=10, prefix="", unique=True
                    ),
                ),
                ("original_url", models.URLField(db_index=True, max_length=2048)),
                (
                    "new_url",
                    models.CharField(
                        blank=True, db_index=True, max_length=10, null=True, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "expires_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2025, 3, 11, 8, 20, 48, 237787, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "URLs",
                "ordering": ["created_at"],
            },
        ),
    ]
