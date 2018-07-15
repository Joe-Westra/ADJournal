from rest_framework import serializers
from .models import NightlyStat

class NightlyStatSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = NightlyStat
        fields = ('id', 'alcohol', 'date')
        read_only_fields = ('date',)
