from pyexpat import model
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    is_included = models.BooleanField(default=True)


class Round(models.Model):
    participants = models.JSONField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()


class Pairs(models.Model):
    first_user = models.CharField(max_length=255)
    second_user = models.CharField(max_length=255)
    meet_happened = models.BooleanField(default=True)
