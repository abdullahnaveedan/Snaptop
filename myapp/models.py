from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    bio = models.CharField(default = "" , max_length=60)
    profilepic = models.ImageField( upload_to="profilepic/" , default = "")
    location = models.CharField(default = "" , max_length=60)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"
    
