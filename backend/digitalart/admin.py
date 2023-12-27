from django.contrib import admin
from .models import Calendar

@admin.register(Calendar)
class CalendarAmdin(admin.ModelAdmin):
    list_display=('id', 'name', 'total_cost', 'prize', 'image','calendars','art_print','order','enabled')
