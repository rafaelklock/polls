from rest_framework import serializers
from .models import Choice, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

