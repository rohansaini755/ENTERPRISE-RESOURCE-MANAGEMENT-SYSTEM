from Products.models import Product,Templates
from rest_framework import serializers

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'