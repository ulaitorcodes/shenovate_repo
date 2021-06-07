from django.db import models

# Create your models here.

class Membership(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    area_of_interest = models.CharField(max_length=50)
    hdyhau = models.CharField(max_length=50)
    why = models.CharField(max_length=50)
    regAt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name
    
