from django.db import models
from django.conf import settings

# Create your models here.
class TextMessage( models.Model):
    speaker = models.CharField(max_length = 20, blank = False)
    message = models.CharField(max_length = 50, blank = True)
    def __str__(self):
        return self.speaker + " " + self.message
