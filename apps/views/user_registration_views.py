import json
from apps.controllers.user_create_controller import UserCreationController
from apps.controllers.user_creation_controller import  UserGameCreationController
from apps.serializers.user_creation_serializer import UserCreationSerializer, UserGameRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserGameRegisterView(APIView):
    def post(self, request):
        ser = UserGameRegisterSerializer(data=request.data)
        ser.is_valid()    
            
        instance = UserGameCreationController(request.data)
        instance()
        
        response_data = instance.result
        return Response(response_data, status=status.HTTP_200_OK)
    
class UserRegisterView(APIView):
    def post(self, request):
        ser = UserCreationSerializer(data=request.data)
        ser.is_valid()    
            
        instance = UserCreationController(request.data)
        instance()
        
        response_data = instance.result
        return Response(response_data, status=status.HTTP_200_OK)
    
