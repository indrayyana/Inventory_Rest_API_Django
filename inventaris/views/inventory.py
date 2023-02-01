from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import Inventory
from inventaris.serializer import InventorySerializer, InventoryShowSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Main(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        inventory_obj = Inventory.objects.all()

        inventory_serializer = InventorySerializer(inventory_obj, many=True)

        return JsonResponse({
            "error": False,
            "data": inventory_serializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):

        body = request.data

        inventory_serializer = InventorySerializer(data={
            "name": body['name'],
            "quantity": body['quantity'],
            "code": body['code'],
            "tipe": body['tipe'],
            "purchase_price": body['purchase_price'],
            "purchase_year": body['purchase_year'],
            "category": body['category_id'],
        })

        if inventory_serializer.is_valid():
            inventory_serializer.save()

            return JsonResponse({
                "error": False,
                "data": inventory_serializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": inventory_serializer.errors
            })
        
class DetailInventory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        inventory_obj = Inventory.objects.filter(id=id).first()

        inventory_serializer = InventoryShowSerializer(inventory_obj)

        return JsonResponse({
            "error": False,
            "data": inventory_serializer.data,
            "message": "Get data successfully"
        })
    
    def put(self, request, id):
        body = request.data

        inventory_obj = Inventory.objects.filter(id=id).first()

        inventory_serializer = InventorySerializer(inventory_obj, data={
            "name": body['name'],
            "quantity": body['quantity'],
            "code": body['code'],
            "tipe": body['tipe'],
            "purchase_price": body['purchase_price'],
            "purchase_year": body['purchase_year'],
            "category": body['category_id'],
        })

        if inventory_serializer.is_valid():
            inventory_serializer.save()

            return JsonResponse({
                "error": False,
                "data": inventory_serializer.data,
                "message": "Data updated successfully"
            })
        
        else: 
            return JsonResponse({
                "error": True,
                "data": None,
                "message": inventory_serializer.errors
            })
        
    def delete(self, request, id):
        inventory_obj = Inventory.objects.filter(id=id).first()

        inventory_obj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data successfully deleted"
        })