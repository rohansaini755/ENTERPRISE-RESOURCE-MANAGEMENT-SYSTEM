from django.db import models

# Create your models here.

class Company(models.Model):
    cmp_id = models.AutoField(primary_key=True)
    cmp_code=models.CharField(max_length=6,unique=True)
    company_name = models.CharField(max_length=100,blank=False,null=False)
    ceo_name = models.CharField(max_length=100,blank=False,null=False)
    dealer_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    dealer_address = models.CharField(max_length=500,blank=True,null=True,default=None)
    dealer_mobile = models.CharField(max_length=12,blank=True,null=True,default=None)
    dealer_whatsapp_mobile = models.CharField(max_length=100,blank=True,null=True,default=None)
    company_type = models.CharField(max_length=100,blank=False,null=False)
    address = models.CharField(max_length=500,blank=False,null=False)
    mobile = models.CharField(unique=True,max_length=20,blank=False,null=False)
    whatsapp_mobile = models.CharField(max_length=12,blank=True,null=True,default=None)
    status = models.IntegerField(default=1)
    email = models.EmailField(blank=True,null=True,default=None)
    added_date = models.DateField(auto_now=True)


    class Meta:
        db_table = 'company'

    # def __str__(self):
    #     return self.first_name
