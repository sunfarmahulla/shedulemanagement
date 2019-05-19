from django.contrib import admin
from .models import ScheduleList, FoodDetails

# Register your models here.

class ScheduleListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'food_name', 'DateTaker', 'TimeTaker')
admin.site.register(ScheduleList, ScheduleListAdmin)

class FoodDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'details', 'gender', 'age', 'file')
admin.site.register(FoodDetails, FoodDetailsAdmin)

"""class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', ' event_id', 'exchange_id', 'event_start', 'event_end', ' event_subject', 'event_location', 'event_category ', 'event_attendees')
admin.site.register(Events, EventstAdmin)"""

