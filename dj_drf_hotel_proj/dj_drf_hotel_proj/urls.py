"""
URL configuration for dj_drf_hotel_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotels.views import (RoomsAPIGetListView,
                          RoomReservationsGetListAPIView, RoomDeleteView, RoomReservationsDeleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/roomslist/", RoomsAPIGetListView.as_view()),
    path("api/v1/roomreservationslist/", RoomReservationsGetListAPIView.as_view()),
    path("api/v1/room/<int:room_id>/", RoomDeleteView.as_view()),
    path("api/v1/roomreservation/<int:booking_id>/", RoomReservationsDeleteView.as_view())
]
