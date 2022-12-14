from rest_framework import serializers
from .models import Cache

class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = ('id', 'name', 'note', 'lat', 'long')