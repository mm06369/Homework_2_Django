from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 200)
    description = models.TextField(null=True, blank=True)
    media = models.CharField(null = True, max_length=200)

    def __str__(self) -> str:
        return self.title
    

