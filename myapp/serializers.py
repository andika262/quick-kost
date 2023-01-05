from rest_framework import serializers
from .models import home

class homeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = home
        fields = '__all__'