from django.shortcuts import render
from rest_framework import generics
from .models import Room, RoomReservation
from .serializers import RoomSerializer, RoomReservationSerializer
# Create your views here.
class RoomsAPIViev(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomReservationsAPIViev(generics.ListAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
