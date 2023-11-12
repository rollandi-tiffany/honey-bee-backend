from django.db import models

class Sitter(models.Model):
    family_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)