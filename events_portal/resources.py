from import_export import resources
from .models import Event
from register.models import Coordinator

class EventResource(resources.ModelResource):
    class Meta:
        model = Event

class CoordinatorResource(resources.ModelResource):
    class Meta:
        model = Coordinator