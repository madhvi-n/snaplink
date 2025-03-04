# Generated by Django 5.1.6 on 2025-03-04 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0002_url_clicks_alter_url_expires_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="one_time_use",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="url",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 3, 11, 9, 30, 36, 54273, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
