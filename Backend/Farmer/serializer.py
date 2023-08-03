from Farmer.models import Farmer
from rest_framework import serializers

class Farmerserializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'