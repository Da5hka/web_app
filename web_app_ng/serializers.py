from rest_framework import serializers
from .models import data_2023, related_papers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class Paperserializer(serializers.ModelSerializer):
    class Meta:
        model = data_2023
        fields = '__all__'
                    
class NG_PPT_serializer(serializers.ModelSerializer):
    class Meta:
        model = related_papers
        fields = ['title_ng_papers', 'description_ng_papers', 'published_ng_papers', 'attach_ng_papers']




                    