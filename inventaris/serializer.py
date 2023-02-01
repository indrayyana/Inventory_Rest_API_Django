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
            'purchase_price',
            'purchase_year'            
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
            'purchase_price',
            'purchase_year',
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
            'inventory',
            'maintenance_date',
            'maintenance_vendor',
            'staff_pic'
        ]

class MaintenanceShowSerializer(serializers.ModelSerializer):
    inventory = InventoryShowSerializer()
    staff_pic = StaffSerializer()
    class Meta:
        model = MaintenanceInventory
        fields = (
            'id',
            'inventory',
            'maintenance_date',
            'maintenance_vendor',
            'staff_pic'
        )