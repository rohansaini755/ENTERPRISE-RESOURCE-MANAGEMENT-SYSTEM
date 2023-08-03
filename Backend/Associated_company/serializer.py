from Associated_company.models import Company
from rest_framework import serializers

class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'