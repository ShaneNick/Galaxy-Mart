from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Custom manager for custom user model
#This manager includes methods to create regular users and super users 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password of the user.
            **extra_fields: Additional model fields as keyword arguments.
            
        Raises:
            ValueError: If no email is provided.
            
        Returns:
            CustomUser: The created user instance.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Custom user model
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)  # Optional
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Other fields and methods...

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']  # Adjusted

    objects = CustomUserManager()

    def __str__(self):
        return self.email

