import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DestinationListView(APIView):
    def post(self, request):
        instance = DestinatiosdfnListView(request.data)
        instance()
        response_data = json.loads(instance.result)
        return Response(response_data, status=status.HTTP_200_OK)
