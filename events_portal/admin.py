from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=('name', 'description', 'date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints')
    list_display = ('name', 'date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints')
    list_filter = ('date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints')
    search_fields = ('name', 'date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints')
    ordering = ('date', 'time', 'location_pref1', 'location_pref2', 'location_pref3', 'mics', 'projector', 'speakers', 'is_event_happening_for_the_first_time', 'judgesheet', 'registration_details', 'PrizeMoney', 'KindPoints')