from django.db import models
from django.contrib import admin
class vehical_db(models.Model):
    Vehical_number=models.CharField(max_length=10,primary_key=True)
    vehical_reg_date=models.DateField()
    Vehical_type=models.CharField(max_length=20)
    Model_number=models.CharField(max_length=10)
    vehical_owner=models.CharField(max_length=30)
    Owner_lis_num=models.CharField(max_length=20)
    Owner_Contact_Num=models.IntegerField()
class vehical_admin(admin.ModelAdmin):
    list_display=["Vehical_number","Vehical_type","Model_number","vehical_owner","Owner_Contact_Num","vehical_reg_date","Owner_lis_num"]