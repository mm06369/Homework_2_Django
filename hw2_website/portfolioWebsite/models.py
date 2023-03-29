from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 200)
    description = models.TextField(null=True, blank=True)
    media = models.ImageField(null=True, blank = True, upload_to='images/')
    def __str__(self) -> str:
        return self.title
    

