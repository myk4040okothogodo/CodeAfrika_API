from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..Communities.models import Community
from ..Lessons.models import Lessons

class Course(models.Model):


    INSTRUCTOR_LED = 1
    ON_DEMAND = 2
    COURSE_CATEGORY = (
        (INSTRUCTOR_LED, _('instructor_led')),
        (ON_DEMAND, _('on_demand')),
            )


    BASIC = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    DIFICULTY_LEVEL = (
        (BASIC, _('Basic')),
        (INTERMEDIATE, _('Intermediate')),
        (ADVANCED, _('Advanced')),
            )

    """A subject of study that is offered by the institution and is examinable."""
    name = models.CharField(max_length= 50, blank=False, null=False)
    Pratical_assesment = models.TextField(blank=False)
    lessons = models.ManyToMany(Lessons)
    course_category = models.PositiveSmallIntegerField(choices=COURSE_CATEGORY, primary_key=True)
    dificulty_level = models.PositiveSmallIntegerField(choices=DIFICULTY_LEVEL, default=BASIC)



    def clean(self):
        if lessons < 2:
            raise ValidationError("The minimum number of lessons per course is two")


    #here we override, django models save method to enforce validation and call full_clean method
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
