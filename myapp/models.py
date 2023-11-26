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
    
class reelsupload(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=50)
    discription = models.CharField(default="", max_length=5000)
    reels = models.ImageField( upload_to="videodata/" , default = "")

    def __str__(self):
        return f"{self.username}"
    