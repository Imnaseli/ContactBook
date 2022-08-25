from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Contact(models.Model ):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = PhoneNumberField(null=False, blank=False)
    alternate_number = PhoneNumberField(max_length=10 ,blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name.title() +" "+ self.last_name.title()
        









 

 



