import json
from apps.controllers.user_creation_controller import UserCreationController
from apps.serializers.user_creation_serializer import UserCreationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserRegisterView(APIView):
    def post(self, request):
        ser = UserCreationSerializer(data=request.data)
        ser.is_valid()    
            
        instance = UserCreationController(request.data)
        instance()
        
        response_data = json.loads(instance.result)
        return Response(response_data, status=status.HTTP_200_OK)
    
