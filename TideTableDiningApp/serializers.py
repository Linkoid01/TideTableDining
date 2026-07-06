from rest_framework import serializers
from .models import (
    Voyage,
    Guest,
    DiningTable,
    DiningSession,
    Reservation,
    ReservationGuest,
)


class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class DiningTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = "__all__"


class DiningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningSession
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class ReservationGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationGuest
        fields = "__all__"