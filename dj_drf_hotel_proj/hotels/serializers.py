from rest_framework import serializers
from datetime import timedelta
from .models import RoomReservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ['booking_id', 'room', 'date_start', 'date_end']
    def validate(self, data):
        room = data.get('room')
        date_start = data.get('date_start')
        date_end = data.get('date_end')

        if date_start and date_end:
            if date_end < date_start:
                raise serializers.ValidationError(
                    "Дата окончания бронирования не может быть раньше даты начала."
                )

            overlapping = RoomReservation.objects.filter(
                room=room,
                date_start__lt=date_end,
                date_end__gt=date_start
            )


            if self.instance:
                overlapping = overlapping.exclude(pk=self.instance.pk)

            if overlapping.exists():
                last_conflict = overlapping.order_by('-date_end').first()
                next_available = last_conflict.date_end + timedelta(days=1)
                raise serializers.ValidationError(
                    f"Номер уже забронирован. Ближайшая доступная дата: {next_available}"
                )

        return data