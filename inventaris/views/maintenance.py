from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import MaintenanceInventory
from inventaris.serializer import MaintenanceSerializer, MaintenanceShowSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Main(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        maintenance_obj = MaintenanceInventory.objects.all()

        maintenance_serializer = MaintenanceSerializer(maintenance_obj, many=True)

        return JsonResponse({
            "error": False,
            "data": maintenance_serializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):

        body = request.data

        maintenance_serializer = MaintenanceSerializer(data={
            "inventory": body['inventory_id'],
            "maintenance_date": body['maintenance_date'],
            "maintenance_vendor": body['maintenance_vendor'],
            "staff_pic": body['staff_pic_id']
        })

        if maintenance_serializer.is_valid():
            maintenance_serializer.save()

            return JsonResponse({
                "error": False,
                "data": maintenance_serializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": maintenance_serializer.errors
            })
        
class DetailMaintenance(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        detail_maintenance_obj = MaintenanceInventory.objects.filter(id=id).first()

        detail_maintenance_serializer = MaintenanceShowSerializer(detail_maintenance_obj)
            
        return JsonResponse({
            "error": False,
            "data": detail_maintenance_serializer.data,
            "message": "Get data successfully"
        })
    
    def put(self, request, id):
        body = request.data

        detail_maintenance_obj = MaintenanceInventory.objects.filter(id=id).first()

        detail_maintenance_serializer = MaintenanceSerializer(detail_maintenance_obj, data={
            'inventory': body['inventory_id'],
            'maintenance_date': body['maintenance_date'],
            'maintenance_vendor': body['maintenance_vendor'],
            'staff_pic': body['staff_pic_id']
        })

        if detail_maintenance_serializer.is_valid():
            detail_maintenance_serializer.save()
            
            return JsonResponse({
                "error": False,
                "data": detail_maintenance_serializer.data,
                "message": "Data updated successfully"
            })
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": detail_maintenance_serializer.errors
            })
        
    def delete(self, request, id):
        detail_maintenance_obj = MaintenanceInventory.objects.filter(id=id).first()

        detail_maintenance_obj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })