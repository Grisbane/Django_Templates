from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Create your models here.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_pics")
    
    def __str__(self):
        return self.user.username
