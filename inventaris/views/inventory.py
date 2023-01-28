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
        inventoryObj = Inventory.objects.all()

        inventorySerializer = InventorySerializer(inventoryObj, many=True).data

        return JsonResponse({
            "error": False,
            "data": inventorySerializer,
            "message": "Get data successfully"
        })

    def post(self, request):

        body = request.data

        inventorySerializer = InventorySerializer(data={
            "id": body['id'],
            "name": body['name'],
            "quantity": body['quantity'],
            "code": body['code'],
            "tipe": body['tipe'],
            "purchasePrice": body['purchasePrice'],
            "purchaseYear": body['purchaseYear'],
            "category": body['category_id'],
        })

        if inventorySerializer.is_valid():
            inventorySerializer.save()

            return JsonResponse({
                "error": False,
                "data": inventorySerializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": inventorySerializer.errors
            })
        
class DetailInventory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        inventoryObj = Inventory.objects.filter(id=id).first()

        inventorySerializer = InventoryShowSerializer(inventoryObj)

        return JsonResponse({
            'error': False,
            'data': inventorySerializer.data
        })
    
    def put(self, request, id):
        body = request.data

        inventoryObj = Inventory.objects.filter(id=id).first()

        inventorySerializer = InventoryShowSerializer(inventoryObj, data={
            "id": body['id'],
            "name": body['name'],
            "quantity": body['quantity'],
            "code": body['code'],
            "tipe": body['tipe'],
            "purchasePrice": body['purchasePrice'],
            "purchaseYear": body['purchaseYear'],
            "category": body['category_id'],
        })

        if inventorySerializer.is_valid():
            inventorySerializer.save()

            return JsonResponse({
                'error': False,
                'data': inventorySerializer.data,
                'message': "Data updated successfully"
            })
        
        else: 
            return JsonResponse({
                'error': True,
                'data': None,
                'message': inventorySerializer.errors
            })
        
    def delete(self, request, id):
        inventoryObj = Inventory.objects.filter(id=id).first()

        inventoryObj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data successfully deleted"
        })