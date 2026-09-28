from django.urls import path
from .views import *

urlpatterns = [
    path('bookings/create/', create_booking),
    path('bookings/', booking_list),
    path('bookings/update/<int:id>/', update_status),
    path('bookings/delete/<int:id>/', delete_booking),
]
