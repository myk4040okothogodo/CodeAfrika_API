from django.db import models

class SchoolModule(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    tasks = models.IntegerField()
