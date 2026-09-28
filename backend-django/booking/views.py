from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Booking Confirmed"})
    return Response(serializer.errors)

@api_view(['GET'])
def booking_list(request):
    bookings = Booking.objects.all().order_by('-id')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_status(request, id):
    booking = Booking.objects.get(id=id)
    booking.status = request.data['status']
    booking.save()
    return Response({"message": "Status Updated"})

@api_view(['DELETE'])
def delete_booking(request, id):
    Booking.objects.get(id=id).delete()
    return Response({"message": "Deleted"})
