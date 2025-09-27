from rest_framework import serializers

from .models import RoomReservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("room_id", "room_number", "description",
                  "price_for_a_night")

class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ("booking_id", "room_id", "date_start",
                  "date_end")