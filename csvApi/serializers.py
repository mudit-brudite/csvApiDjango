from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Question
        fields ="__all__"