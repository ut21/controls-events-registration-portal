from django.db import models
from register.models import Coordinator

venue_choices = (('Online', 'Online'),
        ('Rotunda', 'Rotunda'),
        ('FD2 QT', 'FD2 QT'),
        ('NAB', 'NAB'),)




class Event(models.Model):
    author = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    #club = models.ForeignKey(Coordinator.club, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    #location:
    location_pref1 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    location_pref2 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    location_pref3 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    final_location = models.CharField(max_length=100, choices=venue_choices, default='Online')
    #requisitions:
    mics= models.IntegerField(default=0)
    projector = models.BooleanField(default=False)
    speakers = models.IntegerField(default=0)
    computer_laptop_to_speaker_output_cable_specify_type = models.CharField(max_length=100, blank=True)
    other_requirements = models.TextField(blank=True)
    justify_your_requisitions = models.TextField(blank=True)
    #judgesheetst:
    is_event_happening_for_the_first_time = models.BooleanField(default=False)
    are_external_judges_required = models.BooleanField(default=False)
    will_judges_be_same_for_all_rounds = models.BooleanField(default=False)
    if_Yes_provide_the_details_of_judges = models.TextField(blank=True)
    Number_of_rounds = models.IntegerField(default=0)
    Name_of_round = models.CharField(max_length=100, blank=True)
    expected_participants = models.IntegerField(default=0)
    judgement_criteria_1 = models.TextField(max_length=100, blank=True)
    weightage_1 = models.IntegerField(default=0)
    judgement_criteria_2 = models.TextField(max_length=100, blank=True)
    weightage_2 = models.IntegerField(default=0)
    judgement_criteria_3 = models.TextField(max_length=100, blank=True)
    weightage_3 = models.IntegerField(default=0)
    judgement_criteria_4 = models.TextField(max_length=100, blank=True)
    weightage_4 = models.IntegerField(default=0)
    judgement_criteria_5 = models.TextField(max_length=100, blank=True)
    weightage_5 = models.IntegerField(default=0)
    if_the_above_fields_dont_accomodate_for_your_judgement_criteria_upload_custom_judgesheets = models.FileField(upload_to='judgesheets/',blank=True)
    events_reprography=models.TextField(default="enter events description, rules, and registration details here here. Mention other details like prize money, kind points, etc. also")
    PrizeMoneyRequested=models.IntegerField(default=0)
    KindPointsRequested=models.IntegerField(default=0)
    
    #travels:
    travel_required = models.BooleanField(default=False)
    gender_of_judge = models.CharField(max_length=100, blank=True)
    travel_mode = models.CharField(max_length=100, blank=True)
    travel_date = models.DateField(blank=True)
    travel_time = models.TimeField(blank=True)
    departure_location = models.CharField(max_length=100, blank=True)
    arrival_location = models.CharField(max_length=100, blank=True)
    other_details = models.TextField(blank=True)
    #certs
    certificate_required = models.TextField(blank=True)
    approved=models.BooleanField('Approved', default=False)


    def __str__(self):
        return self.name

