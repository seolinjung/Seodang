from django.db import models
from django.conf import settings
from django.utils import timezone

class Input(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.text
    
class Output(models.Model):
    text = models.CharField(max_length=100)
    hangul = models.OneToOneField(Input, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class HanjaWord(models.Model):
    word = models.CharField(max_length=24)
    sentence = models.ForeignKey(Output, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

class HanjaChar(models.Model):
    char = models.CharField(max_length=1)
    word = models.ForeignKey(HanjaWord, on_delete=models.CASCADE)

    def __str__(self):
        return self.char
    
