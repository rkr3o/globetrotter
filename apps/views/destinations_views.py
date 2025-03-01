import json
from apps.controllers.destination_controller import DestinationController
from apps.serializers.destination_serializer import DestinationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DestinationListView(APIView):
    def post(self, request):
        ser = DestinationSerializer(request.data)
        ser()
        
        instance = DestinationController(request.data)
        instance()
        
        response_data = json.loads(instance.result)
        return Response(response_data, status=status.HTTP_200_OK)
    
