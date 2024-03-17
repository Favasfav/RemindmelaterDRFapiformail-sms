from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Remainder(models.Model):
    choices = (("email", "mail"), ("sms", "sms"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField()
    type_of_remainder = models.CharField(choices=choices, max_length=50)
    
    def __str__(self):
        return str(self.id)
    