from django.db import models
from django.conf import settings
from django.utils import timezone

class Input(models.Model):
    text = models.CharField(max_length=100)
    # date = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
    
    
