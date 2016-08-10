from django.db import models
from django.conf import settings

# Create your models here.


class Log(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=100)
    message = models.TextField()
    name_logger = models.CharField(max_length=100)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
