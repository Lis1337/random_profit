from django.db import models


class Round(models.Model):
    participants = models.JSONField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
