from django.db import models

# Create your models here.

class Farmer(models.Model):
    fm_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    middle_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    father_name = models.CharField(max_length=200,blank=False,null=False)
    gender = models.CharField(max_length=6,default='Male')
    address = models.CharField(max_length=500,blank=False,null=False)
    mobile = models.CharField(unique=True,max_length=12,blank=False,null=False)
    whatsapp_mobile = models.CharField(max_length=12,blank=True,null=True,default=None)
    image = models.CharField(max_length=1000,blank=True,null=True,default=None)
    status = models.IntegerField(default=1)
    email = models.EmailField(blank=True,null=True,default=None)
    city_pincode = models.CharField(max_length=10,blank=True,null=True,default=None)
    added_by = models.IntegerField(default=None,blank=True,null=True)
    added_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'farmer'

    # def __str__(self):
    #     return self.first_name
