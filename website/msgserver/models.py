from django.db import models

# Create your models here.

class Message(models.Model):
    key = models.IntegerField()
    msg = models.TextField()


    def __str__(self):
        return str(self.key) + ': ' + self.msg


