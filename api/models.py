from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        #generates a random code that is 6 length and contains uppercase asci characters
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        #get all our Room objects and filter them by their code member variable
        if Room.objects.filter(code=code).count() == 0:
            #if the amount of Rooms that have a similar code that we just generates is 0 then we have
            # unique code and we can break and leave.
            # else we keep generating a code
            break

    return code

# Create your models here.
class Room(models.Model):
    # Code that we can use to identify a room, generates the code that is unique
    code = models.CharField(max_length=8, default="", unique=True)

    # Infomartion on the host that has the room, one host can have one room
    host = models.CharField(max_length=50, unique=True)

    guest_can_pause = models.BooleanField(null=False, default=False)

    votes_to_skip = models.IntegerField(null=False, default=1)

    # Holds the date and time the room is created at, we don't have to pass in the argument
    created_at = models.DateTimeField(auto_now_add=True)

