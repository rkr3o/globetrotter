import random
from typing import Any
from apps.db_manager.models import Destination, UserGameDetails
from django.db.models import F

from constants.constants_and_methods import RANDOM_DESTINATION, VALIDATE_DESTINATION

class DestinationController:
    def __init__(self, data=None):
        self.data = data or {}
        self.action = self.data.get("action")
        self.user_id = self.data.get("user_id")
        self.user_game_obj,err = UserGameDetails.objects.filter(user_id=self.user_id).get_or_create(user_id=self.user_id)
        self.result = {}
   
    def __call__(self, *args, **kwargs):
        actions = {
            RANDOM_DESTINATION: self.get_random_destination,
            VALIDATE_DESTINATION: lambda: self.validate_answer(self.data.get("user_answer"), self.data.get("clues"), self.data.get("clue_id")),
        }
        return actions.get(self.action, lambda: {})()


    def get_random_destination(self) -> Any:
        destinations = list(Destination.objects.all().values())
        if not destinations:
            return {}

        destination = random.choice(destinations)
        clues = destination.get("clues").get("clues", [])        
        clues_sample = random.sample(clues, min(2, len(clues)))

        self.result =  {
            "clues": clues_sample,
            "clue_id": destination["id"],
            "options": self.get_multiple_choice_options(destination["city"], destinations),
        }
    
    def get_multiple_choice_options(self, correct_city, destinations):
        all_cities = [dest["city"] for dest in destinations if dest["city"] != correct_city]
        random_choices = random.sample(all_cities, min(3, len(all_cities)))
        return random.sample([correct_city] + random_choices, 4)
    
    def get_and_update_user_score(self, obj, **kwargs):
        fields_to_update = []
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
                fields_to_update.append(key)
        if fields_to_update:
            if hasattr(obj, "updated_at"):
                fields_to_update.append("updated_at")
            elif hasattr(obj, "updated"):
                fields_to_update.append("updated")
            obj.save(update_fields=fields_to_update)
    
    
        return obj.correct_score, obj.wrong_score
        
        
    def validate_answer(self, user_answer, clue, clue_id):
        destinations = list(Destination.objects.all().values())  
        correct_city = ""
        for dest in destinations:
            if clue_id == dest["id"]:
                correct_city = dest["city"]
                break

        correct = correct_city.lower() == user_answer.lower()
        message = "🎉 Correct!" if correct else f"😢 Incorrect! The correct answer is {correct_city}."

        fun_fact = random.choice(dest["fun_fact"]["fun_fact"]) if "fun_fact" in dest else ""
        if correct:
            payload = {
                "correct_score": self.user_game_obj.correct_score + 1
            }
        else:
            payload = {
                "wrong_score": self.user_game_obj.wrong_score + 1
            }
        correct_count , wrong_count = self.get_and_update_user_score(self.user_game_obj, **payload)
            
        self.result= {"correct": correct, "message": message, "fun_fact": fun_fact, "correct_count": correct_count, "wrong_count": wrong_count,  "next_button": "Play Again 🎮"}
