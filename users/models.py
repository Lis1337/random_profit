from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    is_included = models.BooleanField(default=True)


class Pairs(models.Model):
    first_user = models.ForeignKey(User, null=False, related_name='first_user', on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, null=False, related_name='second_user', on_delete=models.CASCADE)
    meet_happened = models.BooleanField(default=True)
