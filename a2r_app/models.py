from django.db import models

# Create your models here.

class PurePower(models.Model):
    power = models.IntegerField(primary_key=True)
    roman_rep = models.CharField(max_length=1)

    def __str__(self):
        return "{} as {}".format(self.power, self.roman_rep)


class EdgeCase(models.Model):
    invalid = models.CharField(max_length=5)
    valid = models.CharField(max_length=2)

    def __str__(self):
        return "{}->{}".format(self.invalid, self.valid)
