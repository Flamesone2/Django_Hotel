from rest_framework import serializers

from .models import RoomReservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
# serializers.py
class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ['booking_id', 'room', 'date_start', 'date_end']
    def validate(self, data):
        date_start = data.get('date_start')
        date_end = data.get('date_end')
        if date_start and date_end and date_end < date_start:
            raise serializers.ValidationError(
                "Дата окончания бронирования не может быть раньше даты начала."
            )
        return data