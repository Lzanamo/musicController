from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room

        # id field is a primary key that is a unique int that is automatically made when we make a new model/Room
        # we dont have to define the id field
        fields = ('id', 'code', 'host', 'guest_can_pause', 
                  'votes_to_skip', 'created_at')