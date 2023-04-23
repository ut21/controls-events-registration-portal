from import_export import resources
from .models import Event
from register.models import Coordinator

class EventReqsResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('mics', 'projector', 'speakers', 'computer', 'computer_laptop_to_speaker_output_cable_specify_type', 'other_requirements', 'justify_your_requisitions')
        

class CoordinatorResource(resources.ModelResource):
    class Meta:
        model = Coordinator

class EventResource(resources.ModelResource):
    class Meta:
        model = Event

class EventJudgesheetsResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('is_event_happening_for_the_first_time', 'are_external_judges_required', 'will_judges_be_same_for_all_rounds', 'if_Yes_provide_the_details_of_judges', 'Number_of_rounds', 'Name_of_round', 'expected_participants', 'judgement_criteria_1', 'weightage_1', 'judgement_criteria_2', 'weightage_2', 'judgement_criteria_3', 'weightage_3', 'judgement_criteria_4', 'weightage_4', 'judgement_criteria_5', 'weightage_5', 'if_the_above_fields_dont_accomodate_for_your_judgement_criteria_upload_custom_judgesheets', 'events_reprography', 'PrizeMoenyRequested',)

class EventTravelsResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('travel_required', 'gender_of_judge', 'travel_mode', 'travel_date', 'travel_time', 'departure_location', 'arrival_location', 'other_details')

class EventLocationResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('location_pref1', 'location_pref2', 'location_pref3')