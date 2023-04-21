from django.db import models
from register.models import Coordinator

venue_choices = (('Online', 'Online'),
        ('Rotunda', 'Rotunda'),
        ('FD2 QT', 'FD2 QT'),
        ('NAB', 'NAB'),)




class Event(models.Model):
    author = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location_pref1 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    location_pref2 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    location_pref3 = models.CharField(max_length=100, choices=venue_choices, default='Online')
    mics= models.IntegerField(default=0)
    projector = models.BooleanField(default=False)
    speakers = models.IntegerField(default=0)
    is_event_happening_for_the_first_time = models.BooleanField(default=False)
    #judgesheet field needs to be an excel file
    judgesheet=models.FileField(upload_to='judgesheets/',blank=True)
    registration_details=models.TextField(default="No registration criteria as such")
    PrizeMoney=models.IntegerField(default=0)
    KindPoints=models.IntegerField(default=0)
    approved=models.BooleanField('Approved', default=False)

    def __str__(self):
        return self.name

