from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import Staff
from inventaris.serializer import StaffSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Main(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        staffObj = Staff.objects.all()

        staffSerializer = StaffSerializer(staffObj, many=True)

        return JsonResponse({
            "error": False,
            "data": staffSerializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):

        body = request.data

        staffSerializer = StaffSerializer(data={
            "id": body['id'],
            "name": body['name'],
            "role": body['role'],
        })

        if staffSerializer.is_valid():
            staffSerializer.save()

            return JsonResponse({
                "error": False,
                "data": staffSerializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": staffSerializer.errors
            })
        
class DetailStaff(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        staffObj = Staff.objects.filter(id=id).first()

        staffSerializer = StaffSerializer(staffObj)
        
        return JsonResponse({
            'error': False,
            'data': staffSerializer.data
        })
    
    def put(self, request, id):
        body = request.data

        staffObj = Staff.objects.filter(id=id).first()

        staffSerializer = StaffSerializer(staffObj, data={
            'id': body['id'],
            'name': body['name'],
            'role': body['role']
        })

        if staffSerializer.is_valid():
            staffSerializer.save()
            
            return JsonResponse({
                'error': False,
                'data': staffSerializer.data,
                'message': "Data updated successfully"
            })
        else:
            return JsonResponse({
                'error': True,
                'data': None,
                'message': staffSerializer.errors
            })
        
    def delete(self, request, id):
        staffObj = Staff.objects.filter(id=id).first()

        staffObj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data successfully deleted"
        })