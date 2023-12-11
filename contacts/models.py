# contacts/models.py
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    notes = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
