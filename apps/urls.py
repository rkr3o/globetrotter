from django.urls import path

from apps.views.destinations_views import DestinationListView

urlpatterns = [
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
]