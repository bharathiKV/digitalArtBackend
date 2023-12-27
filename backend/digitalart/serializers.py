from rest_framework import serializers

from .models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calendar
        fields=('id', 'name','total_cost', 'prize', 'image', 'details','calendars','art_print','order','enabled')