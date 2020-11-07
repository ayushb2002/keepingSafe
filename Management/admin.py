from django.contrib import admin
from .models import Data, Location, Appointment, Hospital, Slot, Doctor, Volunteer, Phone
# Register your models here.

admin.site.register(Location)
admin.site.register(Data)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Volunteer)
admin.site.register(Slot)
admin.site.register(Phone)