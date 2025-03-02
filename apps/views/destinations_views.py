import json
from apps.controllers.destination_controller import DestinationController
from apps.serializers.destination_serializer import DestinationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DestinationListView(APIView):
    def post(self, request):
        # import pd b; pdb.set_trace()
        
        data = json.loads(request.body.decode("utf-8"))  # ✅ Parse JSON properly
        
        # ser = DestinationSerializer(data=data)  # ✅ Pass `data` instead of `request.data`
        # ser.is_valid()    

        instance = DestinationController(data)  # ✅ Pass `data`, not `request.data`
        instance()
        
        response_data = instance.result
        return Response(response_data, status=status.HTTP_200_OK)
