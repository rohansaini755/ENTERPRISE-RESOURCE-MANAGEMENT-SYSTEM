from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
     def create_branch(self,phone_number,password,**extra_fields):
          if not phone_number: 
               raise ValueError("User must have phone number")
          
          extra_fields['email'] = self.normalize_email(extra_fields['email'])
          user = self.model(
               phone_number = phone_number,
               **extra_fields
          )
          user.set_password(password)
          user.save()
          return user
    
     def create_superuser(self,phone_number,password,**extra_fields):
          
          extra_fields.setdefault("is_superuser",True)
          extra_fields.setdefault("is_active",True)
          extra_fields.setdefault("main_branch",True)

          if extra_fields.get('is_superuser') is not True:
               raise ValueError("superuser must have superuser value")
          
          return self.create_user(phone_number,password,**extra_fields)

     
class Branch(AbstractUser):
     username        = None
     is_staff        = None
     phone_number    = models.CharField(max_length=12,null=False,unique=True)
     address         = models.CharField(max_length=100,null=False,blank=False,default=None)
     whatsapp_number = models.CharField(max_length=12,null=True,default=None)
     aadhaar_card    = models.CharField(max_length=12,default=None)
     email           = models.EmailField(("email_address"))
     bid             = models.CharField(max_length=50,blank=False,null=False,unique=True)
     main_branch     = models.BooleanField(default=False)

     USERNAME_FIELD  = 'bid'
     REQUIRED_FIELDS = ['phone_number']
     objects         = UserManager()