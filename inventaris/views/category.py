from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from inventaris.models import Category
from inventaris.serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Index(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        category_obj = Category.objects.all()

        category_serializer = CategorySerializer(category_obj, many=True)

        return JsonResponse({
            "error": False,
            "data": category_serializer.data,
            "message": "Get data successfully"
        })

    def post(self, request):
        body = request.data

        category_serializer = CategorySerializer(data={
            "name": body['name']
        })

        if category_serializer.is_valid():
            category_serializer.save()

            return JsonResponse({
                "error": False,
                "data": category_serializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": category_serializer.errors
            })
        
class DetailCategory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        category_obj = Category.objects.filter(id=id).first()

        category_serializer = CategorySerializer(category_obj)
        
        return JsonResponse({
            "error": False,
            "data": category_serializer.data,
            "message": "Get data successfully"
        })
    
    def put(self, request, id):
        body = request.data

        category_obj = Category.objects.filter(id=id).first()

        category_serializer = CategorySerializer(category_obj, data={
            'name': body['name']
        })

        if category_serializer.is_valid():
            category_serializer.save()
            
            return JsonResponse({
                "error": False,
                "data": category_serializer.data,
                "message": "Data updated successfully"
            })
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": category_serializer.errors
            })

    def delete(self, request, id):
        category_obj = Category.objects.filter(id=id).first()
        
        category_obj.delete()

        return JsonResponse({
            "error": False,
            "data": None,
            "message": 'Data successfully deleted'
        })
