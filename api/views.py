from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Making our Api view that is inherited from the generic Api view
# generic api view is a view that is already setup to return to us all of the models
# and we just have to pass is the things we need it to list
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()          #what we want to return
    serializer_class = RoomSerializer      #the format in which we want to return
