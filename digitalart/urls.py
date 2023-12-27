from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.get_calendar_data, name='get_calendar_data'),
]