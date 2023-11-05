from django.db import models
from django.conf import settings
# Create your models here.

class Password(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_passwords'
    )

    def __str__(self):
        return self.title