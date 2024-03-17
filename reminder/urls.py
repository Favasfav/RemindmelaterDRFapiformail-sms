

from django.urls import path
from reminder.views import ReminderViews
urlpatterns = [
    
     path('reminder/',ReminderViews.as_view(), name="reminder"),
]
