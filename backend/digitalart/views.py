from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Calendar
from .serializers import CalendarSerializer

@api_view(['GET'])
def get_calendar_data(request):
    Calendar_data = Calendar.objects.filter(enabled=True)
    serializer = CalendarSerializer(Calendar_data , many=True)
    return Response(serializer.data)
    
