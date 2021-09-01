from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    phone = models.CharField(max_length=14, default="+880")
    image = models.ImageField(upload_to='profiles')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user.username 