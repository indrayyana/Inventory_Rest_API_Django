from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'categories'

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=25, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="relasi_category")
    tipe = models.CharField(max_length=25, blank=False, null=False)
    purchasePrice = models.IntegerField(null=False)
    purchaseYear = models.IntegerField(null=False)

    class Meta:
        db_table = 'inventories'


class Staff(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(max_length=50, null=False, blank=False)

    class Meta: 
        db_table = 'staffs'

class MaintenanceInventory(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    inventoryId = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="relasi_inventory")
    maintenanceDate = models.CharField(max_length=20, null=False, blank=False)
    maintenanceVendor = models.CharField(max_length=50, null=False, blank=False)
    staffPic = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="relasi_staff")

    class Meta:
        db_table = 'maintenance'
