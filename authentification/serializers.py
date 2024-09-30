from rest_framework import serializers
from rest_framework import serializers


from rest_framework import serializers
from rest_framework import serializers


from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from rest_framework import serializers
from .models import Alert
from rest_framework import serializers
from .models import Alert
from django.contrib.gis.geos import Point
class AlertSerializer(serializers.ModelSerializer):
    location = serializers.JSONField()  # To accept GeoJSON data
    
    class Meta:
        model = Alert
        fields = ['alert_type', 'address', 'alert_image', 'location']
    
    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        
        # Parse location if provided
        if location_data:
            coordinates = location_data['coordinates']
            point = Point(coordinates[0], coordinates[1], srid=4326)
            validated_data['location'] = point
        
        alert = Alert.objects.create(**validated_data)
        
        return alert