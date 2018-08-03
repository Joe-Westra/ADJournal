from rest_framework import serializers
from .models import NightlyStat

class NightlyStatSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = NightlyStat
        fields = ('id', 'date', 'alcohol', 'bedtime', 'chores', 'drugs', 'exercise', 'food', 'guitar', 'school', 'work', 'mood_wake', 'mood_sleep', 'notes')
#        read_only_fields = ('date',)
