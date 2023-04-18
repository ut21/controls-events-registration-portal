# Generated by Django 4.2 on 2023-04-18 23:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0003_coordinator_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coordinator",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True
            ),
        ),
    ]