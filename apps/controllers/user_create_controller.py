import random
from typing import Any
from apps.db_manager.models import Destination, User, UserGameDetails
from django.db.models import F

from constants.constants_and_methods import RANDOM_DESTINATION, VALIDATE_DESTINATION, raise_error

class UserCreationController:
    def __init__(self, data=None):
        self.data = data or {}
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.result = {}

    def __call__(self, *args, **kwargs):
        self.check_and_create_user()
    
    def check_and_create_user(self):
        self.user_game_obj, created = User.objects.get_or_create(name=self.name, email = self.email, password = self.password)
        if created:
            self.result = {"user_id": self.user_game_obj.id}
        
