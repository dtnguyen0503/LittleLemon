from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking 

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        #fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = '__all__'
