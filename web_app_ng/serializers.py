from rest_framework import serializers
from .models import data_2023

class NGserializer(serializers.ModelSerializer):
    class Meta:
        model = data_2023
        fields = ['title', 'description', 'picture', 'published', 'cover']