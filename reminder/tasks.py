from celery import shared_task 
from django.core.mail import send_mail
from remindmelater.settings import EMAIL_HOST_USER
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
@shared_task
def schedule_email_task(message, receivers):
    print("message",message,receivers)
    subject = "Reminder Email"
   
    send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently=False)
    return 'done'
@shared_task
def schedule_sms(message):
    print("smsss")

    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body=f' {message}',
    from_='+19517954279',
    to='+919142462970'
    )

    print(message.sid)
    return 'done'