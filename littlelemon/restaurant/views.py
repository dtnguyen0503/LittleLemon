from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, permissions

# Create your views here.
# def sayHello(request):
#     return HttpResponse('Hello World')
def index(request):
    return render(request, 'index.html', {})

# Handles GET (list) and POST (create)
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

# Handle GET (retrieve), PUT (update), and DELETE (delete) for a single item
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
