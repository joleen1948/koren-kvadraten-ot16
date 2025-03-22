from django.db import models
class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

<<<<<<< HEAD
class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
=======
    def __str__(self):
>>>>>>> dae3a4b6b3a6f365ca46362fa2622ea75c4a9444
        return self.name

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
<<<<<<< HEAD

    def _str_(self):
        return self.name
=======
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
>>>>>>> dae3a4b6b3a6f365ca46362fa2622ea75c4a9444
