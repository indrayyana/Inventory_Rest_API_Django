from rest_framework import serializers
from inventaris.models import Category, Inventory, Staff, MaintenanceInventory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'name',
            'quantity',
            'code',
            'category',
            'tipe',
            'purchasePrice',
            'purchaseYear'            
        ]

class InventoryShowSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Inventory
        fields = [
            'id',
            'name',
            'quantity',
            'code',
            'tipe',
            'purchasePrice',
            'purchaseYear',
            'category'            
        ]

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'id',
            'name',
            'role'
        ]

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceInventory
        fields = [
            'id',
            'inventoryId',
            'maintenanceDate',
            'maintenanceVendor',
            'staffPic'
        ]

class MaintenanceShowSerializer(serializers.ModelSerializer):
    inventoryId = InventoryShowSerializer()
    staffPic = StaffSerializer()
    class Meta:
        model = MaintenanceInventory
        fields = (
           'id',
            'inventoryId',
            'maintenanceDate',
            'maintenanceVendor',
            'staffPic'
        )