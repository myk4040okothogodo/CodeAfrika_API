from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    tasks = models.IntegerField() 
