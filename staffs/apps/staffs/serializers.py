from rest_framework import serializers

# local imports
from staffs.apps.staffs.models import RequestsCategory, StaffRequest


class RequestsCategorySerializer(serializers.ModelSerializer):
    """
    Serializer to validate request category details
    """
    class Meta:
        model = RequestsCategory
        fields = ['name', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')


class StaffRequestSerializer(serializers.ModelSerializer):
    """
    Serializer to validate staff requests details
    """
    class Meta:
        model = StaffRequest
        fields = ['request', 'description', 'employee',
                  'status', 'amount', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
