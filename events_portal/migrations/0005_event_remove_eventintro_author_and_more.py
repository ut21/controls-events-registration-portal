# Generated by Django 4.2 on 2023-04-22 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_coordinator_phone'),
        ('events_portal', '0004_eventcerts_eventintro_eventjudgesheets_eventlocation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location_pref1', models.CharField(choices=[('Online', 'Online'), ('Rotunda', 'Rotunda'), ('FD2 QT', 'FD2 QT'), ('NAB', 'NAB')], default='Online', max_length=100)),
                ('location_pref2', models.CharField(choices=[('Online', 'Online'), ('Rotunda', 'Rotunda'), ('FD2 QT', 'FD2 QT'), ('NAB', 'NAB')], default='Online', max_length=100)),
                ('location_pref3', models.CharField(choices=[('Online', 'Online'), ('Rotunda', 'Rotunda'), ('FD2 QT', 'FD2 QT'), ('NAB', 'NAB')], default='Online', max_length=100)),
                ('mics', models.IntegerField(default=0)),
                ('projector', models.BooleanField(default=False)),
                ('speakers', models.IntegerField(default=0)),
                ('computer_laptop_to_speaker_output_cable_specify_type', models.CharField(blank=True, max_length=100)),
                ('other_requirements', models.TextField(blank=True)),
                ('justify_your_requisitions', models.TextField(blank=True)),
                ('is_event_happening_for_the_first_time', models.BooleanField(default=False)),
                ('are_external_judges_required', models.BooleanField(default=False)),
                ('will_judges_be_same_for_all_rounds', models.BooleanField(default=False)),
                ('if_Yes_provide_the_details_of_judges', models.TextField(blank=True)),
                ('Number_of_rounds', models.IntegerField(default=0)),
                ('Name_of_round', models.CharField(blank=True, max_length=100)),
                ('expected_participants', models.IntegerField(default=0)),
                ('judgement_criteria_1', models.TextField(blank=True, max_length=100)),
                ('weightage_1', models.IntegerField(default=0)),
                ('judgement_criteria_2', models.TextField(blank=True, max_length=100)),
                ('weightage_2', models.IntegerField(default=0)),
                ('judgement_criteria_3', models.TextField(blank=True, max_length=100)),
                ('weightage_3', models.IntegerField(default=0)),
                ('judgement_criteria_4', models.TextField(blank=True, max_length=100)),
                ('weightage_4', models.IntegerField(default=0)),
                ('judgement_criteria_5', models.TextField(blank=True, max_length=100)),
                ('weightage_5', models.IntegerField(default=0)),
                ('if_the_above_fields_dont_accomodate_for_your_judgement_criteria_upload_custom_judgesheets', models.FileField(blank=True, upload_to='judgesheets/')),
                ('events_reprography', models.TextField(default='enter events description, rules, and registration details here here. Mention other details like prize money, kind points, etc. also')),
                ('PrizeMoneyRequested', models.IntegerField(default=0)),
                ('KindPointsRequested', models.IntegerField(default=0)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('travel_required', models.BooleanField(default=False)),
                ('gender_of_judge', models.CharField(blank=True, max_length=100)),
                ('travel_mode', models.CharField(blank=True, max_length=100)),
                ('travel_date', models.DateField(blank=True)),
                ('travel_time', models.TimeField(blank=True)),
                ('departure_location', models.CharField(blank=True, max_length=100)),
                ('arrival_location', models.CharField(blank=True, max_length=100)),
                ('other_details', models.TextField(blank=True)),
                ('certificate_required', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.coordinator')),
            ],
        ),
        migrations.RemoveField(
            model_name='eventintro',
            name='author',
        ),
        migrations.RemoveField(
            model_name='eventjudgesheets',
            name='author',
        ),
        migrations.RemoveField(
            model_name='eventlocation',
            name='author',
        ),
        migrations.RemoveField(
            model_name='eventrequisitions',
            name='author',
        ),
        migrations.RemoveField(
            model_name='eventtravels',
            name='author',
        ),
        migrations.DeleteModel(
            name='EventCerts',
        ),
        migrations.DeleteModel(
            name='EventIntro',
        ),
        migrations.DeleteModel(
            name='EventJudgesheets',
        ),
        migrations.DeleteModel(
            name='EventLocation',
        ),
        migrations.DeleteModel(
            name='EventRequisitions',
        ),
        migrations.DeleteModel(
            name='EventTravels',
        ),
    ]
