from django.db import models


class Task(models.Model):
    body = models.TextField()
    is_finished = models.BooleanField(default=False)
    estimated_finish_time = models.DateTimeField()
