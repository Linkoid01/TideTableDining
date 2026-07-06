from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "tide_table_dining"

router = DefaultRouter()
router.register(r"voyages", views.VoyageViewSet)
router.register(r"guests", views.GuestViewSet)
router.register(r"tables", views.DiningTableViewSet)
router.register(r"sessions", views.DiningSessionViewSet)
router.register(r"reservations", views.ReservationViewSet)
router.register(r"reservation-guests", views.ReservationGuestViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("api/", include(router.urls)),
]