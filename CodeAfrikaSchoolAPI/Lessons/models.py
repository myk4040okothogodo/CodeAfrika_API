from django.db import models
from django.conf import settings
# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    instructor = models.OneToOneField(settings.AUTH_USER_MODEL)
    students = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"
