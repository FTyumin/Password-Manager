from django.db import models

# Create your models here.

class Password(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField("auth.User",
                                on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title