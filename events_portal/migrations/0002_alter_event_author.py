# Generated by Django 4.2 on 2023-04-19 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_coordinator_phone'),
        ('events_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.coordinator'),
        ),
    ]
