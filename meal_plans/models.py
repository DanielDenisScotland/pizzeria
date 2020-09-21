from django.db import models

# Create your models here.


class Day(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        """return a string representing the model"""
        return self.text


class Meal(models.Model):
    """Some specific learnt about a model"""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """return a string representing the model"""
        return self.text
