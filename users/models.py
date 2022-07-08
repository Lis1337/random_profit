from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)


class Round(models.Model):
    participants = models.JSONField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()


class Pairs(models.Model):
    first_user = models.ForeignKey(User)
    second_user = models.ForeignKey(User)
    meet_happened = models.BooleanField(default=False)