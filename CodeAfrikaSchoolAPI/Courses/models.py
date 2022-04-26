from django.db import models
from ..Communities.models import Community


class Course(models.Model):
    """A subject of study that is offered by the institution and is examinable."""
    name = models.CharField(max_length= 50, blank=False, null=False)
    
