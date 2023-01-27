from django.http import JsonResponse
from rest_framework.views import APIView
from user.models import User

from user.serializer import UserSerializer

from django.contrib.auth.hashers import make_password
# from rest_framework.permissions import a

class UserList(APIView):
    
    def get(self, request):
        
        userObj = User.objects.all()
     
        userSerializer = UserSerializer(userObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": userSerializer.data,
            "message": "Get data successfully"
        })
        
    def post(self, request):
        
        body = request.data 
      
        
        userSerializer = UserSerializer(data={
            "name": body['name'],
            "username": body['username'],
            "password": make_password(password=body['password'])
        })
        
        if userSerializer.is_valid():
            userSerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": userSerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            
            return JsonResponse({
                "error": True,
                "data": None,
                "message": userSerializer.errors
            })

    
class UserDetail(APIView):
    
    def get(self, request, id):
        
        userObj = User.objects.filter(id=id).first()
        
        userSerializer = UserSerializer(userObj)
        
        return JsonResponse({
            "error": False,
            "data": userSerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        userObj = User.objects.filter(id=id).first()
        
        userSerializer = UserSerializer(userObj, data={
            "name": body['name'],
            "username": body['username'],
            "password": make_password(password=body['password'])
        })
        
        if userSerializer.is_valid():
            userSerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": userSerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": userSerializer.errors
            })
            
    def delete(self, request, id):
        
        userObject = User.objects.filter(id=id).first()
        
        userObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })