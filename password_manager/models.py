from django.db import models

# Create your models here.

class Password(models.Model):
    title = models.CharField(max_length=200)
    password = models.TextField()

    def __str__(self):
        return self.title