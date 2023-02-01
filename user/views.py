from django.http import JsonResponse
from rest_framework.views import APIView
from user.models import User
from user.serializer import UserSerializer
from django.contrib.auth.hashers import make_password

class UserList(APIView):
    
    def get(self, request):
        
        user_obj = User.objects.all()
     
        user_serializer = UserSerializer(user_obj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": user_serializer.data,
            "message": "Get data successfully"
        })
        
    def post(self, request):
        
        body = request.data 
        
        user_serializer = UserSerializer(data={
            "name": body['name'],
            "username": body['username'],
            "password": make_password(password=body['password'])
        })
        
        if user_serializer.is_valid():
            user_serializer.save()
            
            return JsonResponse({
              "error": False,
              "data": user_serializer.data,
              "message": "Data saved successfully"
            })
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "message": user_serializer.errors
            })

    
class UserDetail(APIView):
    
    def get(self, request, id):
        
        user_obj = User.objects.filter(id=id).first()
        
        user_serializer = UserSerializer(user_obj)
        
        return JsonResponse({
            "error": False,
            "data": user_serializer.data,
            "message": "Get data successfully"
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        user_obj = User.objects.filter(id=id).first()
        
        user_serializer = UserSerializer(user_obj, data={
            "name": body['name'],
            "username": body['username'],
            "password": make_password(password=body['password'])
        })
        
        if user_serializer.is_valid():
            user_serializer.save()
            
            return JsonResponse({
                "error": False,
                "data": user_serializer.data,
                "message": "Data updated successfully"
            })
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": user_serializer.errors
            })
            
    