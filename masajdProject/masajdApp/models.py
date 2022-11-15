from django.db import models
from location_field.models.plain import PlainLocationField 

# Create your models here.
class problem (models.Model):
    mosque_name= models.CharField(max_length=512)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    PhoneNum= models.IntegerField()
    Description =models.TextField()
    #image = models.ImageField(upload_to="images/") 