# Generated by Django 5.1.6 on 2025-04-03 13:26

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0006_alter_url_expires_at_alter_url_new_url"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="url",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 4, 10, 13, 26, 31, 804715, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
