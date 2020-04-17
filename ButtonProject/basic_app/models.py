from django.db import models
import django.db.models.deletion
from django.utils import timezone


# Create your models here.

class SystemStatus(models.Model):
    status = models.BooleanField(default=False)
    #date_changed = models.DateField(default=timezone.now())
    date_changed = models.DateField()
