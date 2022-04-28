from django.db import models
from django.conf import settings
# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    instructor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="instructor_teaching_lesson")
    students = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="students_taking_lesson")


    def __str__(self):
        return f"{self.name}"
