from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self,user_name,email,first_name,last_name,dob,password,**other_fields):
        
        if not email:
            raise ValueError("Email ain't valid")
        
        email = self.normalize_email(email)
        user = self.model(
            user_name=user_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            **other_fields,
            )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,user_name,email,first_name,last_name,dob,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        return self.create_user(user_name,email,first_name,last_name,dob,password,**other_fields)

class MyUser(AbstractBaseUser, PermissionsMixin) :
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    dob = models.DateField()
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    # password = models.CharField(max_length=50, default="password")
    # profilePicture = models.ImageField(upload_to='images/', default='default')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name','dob']

    def __str__(self) :
        return self.first_name

class Entry(models.Model) :
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=254)
    text = models.TextField()
    created = models.DateTimeField('date published')
    # last_modified = models.DateTimeField
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.title
