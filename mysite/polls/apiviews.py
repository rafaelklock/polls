from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Question, Choice
from .serializers import QuestionSerializer


class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        data = QuestionSerializer(questions, many=True,).data
        return Response(data)


class QuestionDetail(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        data = QuestionSerializer(question).data
        return Response(data)


