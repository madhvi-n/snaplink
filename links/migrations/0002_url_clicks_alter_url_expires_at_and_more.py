# Generated by Django 5.1.6 on 2025-03-04 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="clicks",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="url",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 3, 11, 8, 54, 41, 565161, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="url",
            name="original_url",
            field=models.URLField(db_index=True, max_length=2048, unique=True),
        ),
    ]
