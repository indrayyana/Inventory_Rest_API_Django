from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'categories'

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=25, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="relasi_category")
    tipe = models.CharField(max_length=25, blank=False, null=False)
    purchase_price = models.IntegerField(null=False)
    purchase_year = models.IntegerField(null=False)

    class Meta:
        db_table = 'inventories'


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(max_length=50, null=False, blank=False)

    class Meta: 
        db_table = 'staffs'

class MaintenanceInventory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="relasi_inventory")
    maintenance_date = models.CharField(max_length=20, null=False, blank=False)
    maintenance_vendor = models.CharField(max_length=50, null=False, blank=False)
    staff_pic = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="relasi_staff")

    class Meta:
        db_table = 'maintenance'
