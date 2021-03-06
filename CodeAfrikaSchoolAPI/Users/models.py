from django.db import models
from  django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """ Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """ Create and return a `user` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email')
        if username is None:
            raise TypeError('Superusers must have a username.')

        user = self.create_user(username, email, password)
        user.is_superuser =  True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Role(models.Model):
    """
    The Role entries are managed by the system automatically created via a Django data migration
    """
    CONTRIBUTOR = 1
    MEMBER      = 2
    ADMIN       = 3
    ROLE_CHOICES = (
        (CONTRIBUTOR, 'contributor'),
        (MEMBER, 'member',),
        (ADMIN, 'admin'),
                )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    def __str__(self):
        return self.get_id_display()




class User(AbstractBaseUser, PermissionsMixin):

    BASIC = 1
    PREMIUM = 2
    MEMBERSHIP_PLANS = (
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    roles = models.ManyToManyField(Role)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    #check if user is a has a member role, then assign membeership_plan
    membership_plan = models.PositiveIntegerField(choices=MEMBERSHIP_PLANS)
    phone_number = PhoneNumberField(default = "+***********")
        
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


