from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Room, RoomReservation
from .serializers import RoomSerializer, RoomReservationSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


class RoomsAPIGetListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"room_id": serializer.instance.room_id},
                        status=status.HTTP_201_CREATED)

class RoomDeleteView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    lookup_field = "room_id"


class RoomReservationsGetListAPIView(generics.ListCreateAPIView):
    serializer_class = RoomReservationSerializer

    def get_queryset(self):

        room_id = self.request.query_params.get("room_id")
        if room_id is None:
            return RoomReservation.objects.all()

        get_object_or_404(Room, room_id=room_id)
        return RoomReservation.objects.filter(room_id=room_id)

class RoomReservationsDeleteView(generics.DestroyAPIView):
    queryset = RoomReservation.objects.all()
    lookup_field = "booking_id"