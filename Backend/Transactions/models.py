from django.db import models
from Farmer.models import Farmer

# Create your models here.
class Transactions(models.Model):
    tns_id = models.AutoField(primary_key=True)
    fm_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    tns_date = models.DateTimeField(auto_now_add=True)
    fm_mobile = models.CharField(max_length=12,null=False,blank=False)
    product_list = models.CharField(max_length=1000,null=False,blank=False)
    total_transaction = models.IntegerField(null=False,blank=False)
    paydown = models.IntegerField(null=False,blank=False,default=0)
    total_due = models.IntegerField(null=False,blank=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'transactions'

