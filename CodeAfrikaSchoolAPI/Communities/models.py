from django.db import models
from django.conf import settings
from  ..Topics.models import Topic
from  ..Courses.models import Course
from  ..Projects.models import Project
#from ..Articles.models import Article

class Community(models.Model):
    """A community that is made up of mambers with common interests."""
    name  = models.CharField(max_length= 50, blank=False, null=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="members_of_thiscommunity")
    topics = models.ManyToManyField(Topic)
    community_champion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="champion_of_thiscommunity")
    projects = models.ManyToManyField(Project)
    courses = models.ManyToManyField(Course)
    #articles = models.ManyToMany(Article)


    def __str__(self):
        return f"{self.name}"



