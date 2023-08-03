from django.db import models
from Associated_company.models import Company
# from .models import Product

# Create your models here.
class Product(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_company = models.ForeignKey(Company,on_delete=models.CASCADE)
    pr_name = models.CharField(max_length=100,null=False,blank=False)
    pr_salt = models.CharField(max_length=500,null=True,blank=True,default="")
    pr_detail = models.CharField(max_length=500,null=True,blank=True,default="")
    pr_instructions = models.CharField(max_length=1000,null=True,blank=True,default="")
    pr_type = models.CharField(max_length=55,null=False,blank=False)
    pr_price = models.IntegerField(default=0)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'product'

class Templates(models.Model):
    tmp_id =  models.AutoField(primary_key=True)
    tmp_name = models.CharField(max_length=100,null=False,blank=False,default=None)
    tmp_description = models.CharField(max_length=1000,null=True,blank=True,default=None)
    status = models.BooleanField(default=True)
    tmp_pr_1 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr1",null=True,default=None)
    tmp_pr_2 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr2",null=True,default=None)
    tmp_pr_3 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr3",null=True,default=None)
    tmp_pr_4 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr4",null=True,default=None)
    tmp_pr_5 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr5",null=True,default=None)
    tmp_pr_6 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr6",null=True,default=None)
    tmp_pr_7 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr7",null=True,default=None)
    tmp_pr_8 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr8",null=True,default=None)
    tmp_pr_9 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr9",null=True,default=None)
    tmp_pr_10 = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="template_pr10",null=True,default=None)

    class Meta:
        db_table = 'template'
