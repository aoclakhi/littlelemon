from django.urls import path
from .views import (
    MenuView,
    SingleMenuView,
    BookingView,
    SingleBookingView
)

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuView.as_view()),

    path('booking/', BookingView.as_view()),
    path('booking/<int:pk>', SingleBookingView.as_view()),
]