from rest_framework import serializers
from Branch.models import Branch
class BranchSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length = 6,write_only=True,required=True
    )
    class Meta:
        model = Branch
        fields = '__all__'

    