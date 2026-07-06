from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from .models import (
    Voyage,
    Guest,
    DiningTable,
    DiningSession,
    Reservation,
    ReservationGuest,
)
from .serializers import (
    VoyageSerializer,
    GuestSerializer,
    DiningTableSerializer,
    DiningSessionSerializer,
    ReservationSerializer,
    ReservationGuestSerializer,
)

def home(request):
    return HttpResponse("TideTable Dining – Proof of Concept")

class VoyageViewSet(viewsets.ModelViewSet):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class DiningTableViewSet(viewsets.ModelViewSet):
    queryset = DiningTable.objects.all()
    serializer_class = DiningTableSerializer


class DiningSessionViewSet(viewsets.ModelViewSet):
    queryset = DiningSession.objects.all()
    serializer_class = DiningSessionSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationGuestViewSet(viewsets.ModelViewSet):
    queryset = ReservationGuest.objects.all()
    serializer_class = ReservationGuestSerializer