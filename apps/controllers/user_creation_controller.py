import random
from typing import Any
from apps.db_manager.models import Destination, UserGameDetails
from django.db.models import F

from constants.constants_and_methods import RANDOM_DESTINATION, VALIDATE_DESTINATION, raise_error

class UserGameCreationController:
    def __init__(self, data=None):
        self.data = data or {}
        self.action = self.data.get("action")
        self.user_id = self.data.get("user_id")  
        self.result = {}

    def __call__(self, *args, **kwargs):
        self.check_for_existing_user()
        self.update_or_create_user()
    
    def check_for_existing_user(self):
        if UserGameDetails.objects.filter(user_id=self.user_id).exists():
            raise_error(4, "This user already exists in the system, please use a different user ID", 400)
            
    def update_or_create_user(self):
        self.user_game_obj, created = UserGameDetails.objects.get_or_create(user_id=self.user_id)
        if created:
            print("New user created successfully!")
        else:
            print("User already exists, skipping creation.")
