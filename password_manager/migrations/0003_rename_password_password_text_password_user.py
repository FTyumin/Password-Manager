# Generated by Django 4.2.5 on 2023-11-05 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("password_manager", "0002_rename_body_password_password"),
    ]

    operations = [
        migrations.RenameField(
            model_name="password",
            old_name="password",
            new_name="text",
        ),
        migrations.AddField(
            model_name="password",
            name="user",
            field=models.ForeignKey(
                default="admin",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_passwords",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]