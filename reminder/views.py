from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from reminder.serializers import RemainderSerialir
from .tasks import schedule_email_task,schedule_sms
from datetime import datetime
from django.utils import timezone
class ReminderViews(APIView):
    def post(self, request, format=None):
        try:
            serializer = RemainderSerialir(data=request.data)
            if serializer.is_valid():
                serializer.save()
                date_time = datetime.strptime(request.data.get("date_time"), '%Y-%m-%d %H:%M:%S')
                date_time = timezone.make_aware(date_time, timezone.get_current_timezone())  # Make date_time aware
                if date_time >= timezone.now():
                    print("date_time",date_time,'===========',timezone.now())
                    if request.data.get('type_of_remainder') == 'email':
                        
                            # schedule_email_task(request.data.get('message'), "default@gmail.com")
                            # schedule_email_task.apply_async(kwargs={"message": request.data.get('message'), "receivers": "default@gmail.com"}, eta=date_time)
                            schedule_email_task.apply_async((request.data.get('message'),"default@gmail.com"),countdown=2)  # date_object or eta=current_datetime

                            return Response(serializer.data, status=status.HTTP_201_CREATED)

                            
                    elif request.data.get('type_of_remainder') == 'sms':
                        schedule_sms.apply_async((request.data.get('message'),), eta=date_time)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "Invalid date/time."},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)