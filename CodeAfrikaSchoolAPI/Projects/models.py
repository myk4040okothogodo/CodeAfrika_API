from django.db import models
from django.utils.translation import ugettext_lazy as _
#from ..School_Modules.users import School_Module
# Create your models here.


class Project(models.Model):
    PYTHON  = 1
    JAVA    = 2
    JAVASCRIPT = 3
    RUST    = 4
    GOLANG  = 5
    C_PLUSPLUS     = 6
    C       = 7
    SOLIDITY= 8
    LANGUAGE = (
        (PYTHON, _('python')),
        (JAVA,   _('java')),
        (JAVASCRIPT, _('javascript')),
        (RUST, _('rust')),
        (GOLANG, _('golang')),
        (C_PLUSPLUS , _('c_plusplus')),
        (SOLIDITY, _('solidity')),
            )

    name = models.CharField(max_length= 30, blank=False)
    language = models.PositiveSmallIntegerField(choices=LANGUAGE, default=PYTHON)
    #schoolmodules = models.ForeignKey(School_Module, on_delete=models.CASCADE)



    def clean(self):
        if len(modules) < 2:
            raise ValidationError("Each Project  must contain atleast two modules")
    

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
