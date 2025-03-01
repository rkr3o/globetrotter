from django.urls import path

from apps.views.destinations_views import DestinationListView
from apps.views.user_registration_views import UserRegisterView


urlpatterns = [
    path('destinations', DestinationListView.as_view(), name='destination-list'),
    path('users/register', UserRegisterView.as_view(), name='user-register'),
]