from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10)
    alternate_number = models.CharField(max_length=10, blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    









 

 



