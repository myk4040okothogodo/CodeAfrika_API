from django.db import models
from django.conf import settings
from  ..Topic.models import Topic
from  ..Courses.models import Course
from  ..Projects.models import Project
from ..Articles.models import Article

class Community(models.Model):
    """A community that is made up of mambers with common interests."""
    name  = models.CharField(max_length= 50, blak=False, null=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    topics = models.ManyToManyField(Topic)
    community_champion = models.ForeignKey(settings.AUTH_USER_MODEL)
    projects = models.ManyToMany(Project)
    courses = models.ManyToMany(Course)
    articles = models.ManyToMany(Article)


    def __str__(self):
        return f"{self.name}"



