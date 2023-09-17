from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,first_name, last_name,user_name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not user_name:
            raise ValueError('Users must have an user_name')
        
        user = self.model(
            email=self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name, last_name, user_name, email, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    
    class User(AbstractBaseUser):
        CONTRIBUTOR = 1
        ADMIN = 2
        first_name = models.CharField(max_length=50)
        last_name =models.CharField(max_length=50)
        username = models.CharField(max_length=50)
        email = models.EmailField(max_length=100, unique=True)
        phone_number = models.CharField(max_length=50)
        role = models.PositiveSmallIntegerField(default=CONTRIBUTOR, blank=True, null=True)
        
        # required fields
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(auto_now_add=True)
        created_date = models.DateTimeField(auto_now_add=True)
        modified_date = models.DateTimeField(auto_now=True)
        is_admin = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=False)
        is_superadmin = models.BooleanField(default=False)
        
        
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
        
        def __str__(self):
            return self.email
        
        def has_perm(self, perm, obj=None):
            return self.is_admin
        
        def has_module_perms(self, add_label):
            return True
        
        objects = UserManager()
        
        # Context from Class or Interface c:/Users/NEKIWANUKA/Desktop/fgf-repo/auth_app/models copy.py:User_Contribution