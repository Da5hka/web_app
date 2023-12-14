from rest_framework import serializers
from .models import data_2023, related_papers

class Paperserializer(serializers.ModelSerializer):
    class Meta:
        model = data_2023
        fields = '__all__'
                    
class NG_PPT_serializer(serializers.ModelSerializer):
    class Meta:
        model = related_papers
        fields = ['title_ng_papers', 'description_ng_papers', 'published_ng_papers', 'attach_ng_papers']

