from django.db import models
from django.core.validators import MaxValueValidator

class Sitter(models.Model):
    family_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    children_age = models.IntegerField(validators=[MaxValueValidator(15)], default=0)
    hourly_wage = models.DecimalField(max_digits=5, decimal_places=2, default=20)
