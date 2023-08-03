from Transactions.models import Transactions
from rest_framework import serializers

class Transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'