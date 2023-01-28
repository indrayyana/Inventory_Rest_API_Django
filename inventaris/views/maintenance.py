from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import MaintenanceInventory
from inventaris.serializer import MaintenanceSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Main(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        maintenanceObj = MaintenanceInventory.objects.all()

        maintenanceSerializer = MaintenanceSerializer(maintenanceObj, many=True)

        return JsonResponse({
            "error": False,
            "data": maintenanceSerializer.data
        })

    def post(self, request):

        body = request.data

        maintenanceSerializer = MaintenanceSerializer(data={
            "inventoryId": body['inventoryId'],
            "maintenanceDate": body['maintenanceDate'],
            "maintenanceVendor": body['maintenanceVendor'],
            "staffPic": body['staffPic']
        })

        if maintenanceSerializer.is_valid():
            maintenanceSerializer.save()

            return JsonResponse({
                "error": False,
                "data": maintenanceSerializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": maintenanceSerializer.errors
            })
        
class DetailMaintenance(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        def get(self, request, id):
            detailMaintenanceObj = MaintenanceInventory.objects.filter(id=id).first()

            detailMaintenanceSerializer = MaintenanceSerializer(detailMaintenanceObj).data
            
            return JsonResponse({
                'error': False,
                'data': detailMaintenanceSerializer
            })
    
    def put(self, request, id):
        body = request.data

        detailMaintenanceObj = MaintenanceInventory.objects.filter(id=id).first()

        detailMaintenanceSerializer = MaintenanceSerializer(detailMaintenanceObj, data={
            'id': body['id'],
            'inventoryId': body['inventoryId'],
            'maintenanceDate': body['maintenanceDate'],
            'maintenanceVendor': body['maintenanceVendor'],
            'staffPic': body['staffPic']
        })

        if detailMaintenanceSerializer.is_valid():
            detailMaintenanceSerializer.save()
            
            return JsonResponse({
                'error': False,
                'data': detailMaintenanceSerializer.data,
                'message': "Data updated successfully"
            })
        else:
            return JsonResponse({
                'error': True,
                'data': None,
                'message': detailMaintenanceSerializer.errors
            })
        
    def delete(self, request, id):
        detailMaintenanceObj = MaintenanceInventory.objects.filter(id=id).first()

        detailMaintenanceObj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data successfully deleted"
        })