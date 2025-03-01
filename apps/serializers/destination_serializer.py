from typing import Any
from rest_framework import serializers

class DestinationSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        return {}
    
    def to_representation(self, instance):
        return {}