from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email_id = models.EmailField(max_length=150)
    phone_no = models.IntegerField()
    
    def __str__(self):
        return self.name
    

