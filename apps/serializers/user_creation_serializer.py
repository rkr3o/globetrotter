from typing import Any
from constants.constants_and_methods import RANDOM_DESTINATION, VALIDATE_DESTINATION, raise_error
from rest_framework import serializers

class UserCreationSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if not data:
            raise_error(1, "No data provided", 400)
    
    def to_representation(self, instance):
        return {}
    
class UserGameRegisterSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if not data:
            raise_error(1, "No data provided", 400)
        
        if not data.get("user_id"):
            raise_error(3, "user_id is missing", 400)
            
    
    def to_representation(self, instance):
        return {}