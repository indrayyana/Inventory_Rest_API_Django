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
        categoryObj = Category.objects.all()

        categorySerializer = CategorySerializer(categoryObj, many=True).data

        return JsonResponse({
            "error": False,
            "data": categorySerializer,
            "message": "Get data successfully"
        })

    def post(self, request):
        body = request.data

        categorySerializer = CategorySerializer(data={
            "id": body['id'],
            "name": body['name']
        })

        if categorySerializer.is_valid():
            categorySerializer.save()

            return JsonResponse({
                "error": False,
                "data": categorySerializer.data,
                "message": "Data saved successfully"
            })
        
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": categorySerializer.errors
            })
        
class DetailCategory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        categoryObj = Category.objects.filter(id=id).first()

        categorySerializer = CategorySerializer(categoryObj).data
        
        return JsonResponse({
            'error': False,
            'data': categorySerializer
        })
    
    def put(self, request, id):
        body = request.data

        categoryObj = Category.objects.filter(id=id).first()

        categorySerializer = CategorySerializer(categoryObj, data={
            'id': body['id'],
            'name': body['name']
        })

        if categorySerializer.is_valid():
            categorySerializer.save()
            
            return JsonResponse({
                'error': False,
                'data': categorySerializer.data,
                'message': "Data updated successfully"
            })
        else:
            return JsonResponse({
                'error': True,
                'data': None,
                'message': categorySerializer.errors
            })

    def delete(self, request, id):
        categoryObj = Category.objects.filter(id=id).first()
        
        categoryObj.delete()

        return JsonResponse({
            'error': False,
            'data': None,
            'message': 'Data successfully deleted'
        })
