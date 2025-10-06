from django.db import models

# Create your models here.
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
    price_for_a_night = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата добавления номера")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата изменения номера")



class RoomReservation(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
