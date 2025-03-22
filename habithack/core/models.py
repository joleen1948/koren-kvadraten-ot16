from django.db import models

class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.name

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.name
