from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import Staff
from inventaris.serializer import StaffSerializer, StaffShowSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Main(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        staff_obj = Staff.objects.all()

        staff_serializer = StaffSerializer(staff_obj, many=True)

        return JsonResponse({
            "error": False,
            "data": staff_serializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):

        body = request.data

        staff_serializer = StaffSerializer(data={
            "name": body['name'],
            "role": body['role'],
        })

        if staff_serializer.is_valid():
            staff_serializer.save()

            return JsonResponse({
                "error": False,
                "data": staff_serializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": staff_serializer.errors
            })
        
class DetailStaff(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        staff_obj = Staff.objects.filter(id=id).first()

        staff_serializer = StaffShowSerializer(staff_obj)
        
        return JsonResponse({
            "error": False,
            "data": staff_serializer.data,
            "message": "Get data successfully"
        })
    
    def put(self, request, id):
        body = request.data

        staff_obj = Staff.objects.filter(id=id).first()

        staff_serializer = StaffSerializer(staff_obj, data={
            'name': body['name'],
            'role': body['role']
        })

        if staff_serializer.is_valid():
            staff_serializer.save()
            
            return JsonResponse({
                "error": False,
                "data": staff_serializer.data,
                "message": "Data updated successfully"
            })
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": staff_serializer.errors
            })
        
    def delete(self, request, id):
        staff_obj = Staff.objects.filter(id=id).first()

        staff_obj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })