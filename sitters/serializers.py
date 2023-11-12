from .models import Sitter
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class SitterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sitter
        fields = ['id', 'family_name', 'details']