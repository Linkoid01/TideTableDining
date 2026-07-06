from django.db import models


class Voyage(models.Model):

    # Django will create an AutoField primary key named "id" by default.
    VoyageCode = models.CharField(max_length=32, unique=True)
    Status = models.CharField(max_length=32)

    def __str__(self):
        return self.VoyageCode


class Guest(models.Model):

    Voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name="guests")
    BookingNumber = models.CharField(max_length=64)
    PMSGuestID = models.CharField(max_length=64)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    CabinNumber = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.BookingNumber})"


class DiningTable(models.Model):

    TableNumber = models.CharField(max_length=16, unique=True)
    Capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.TableNumber} (cap {self.Capacity})"


class DiningSession(models.Model):

    Voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name="sessions")
    ServiceDate = models.DateField()
    MealPeriod = models.CharField(max_length=32)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Status = models.CharField(max_length=32)

    class Meta:
        ordering = ["ServiceDate", "StartTime"]

    def __str__(self):
        return f"{self.Voyage.VoyageCode} {self.ServiceDate} {self.MealPeriod}"


class Reservation(models.Model):

    Voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name="reservations")
    Session = models.ForeignKey(DiningSession, on_delete=models.CASCADE, related_name="reservations")
    Table = models.ForeignKey(DiningTable, on_delete=models.PROTECT, related_name="reservations")
    PartySize = models.PositiveIntegerField()
    Status = models.CharField(max_length=32)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-CreatedAt"]

    def __str__(self):
        return f"Reservation {self.pk} ({self.PartySize} pax)"


class ReservationGuest(models.Model):

    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation_guests")
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="guest_reservations")
    IsLeadGuest = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            ("Reservation", "Guest"),
        )

    def __str__(self):
        role = "Lead" if self.IsLeadGuest else "Guest"
        return f"{role} {self.Guest} for {self.Reservation}"