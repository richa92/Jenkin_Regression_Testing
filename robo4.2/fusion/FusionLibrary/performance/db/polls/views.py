from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice, Question
from rest_framework import viewsets
from serializers import ChoiceSerializer, QuestionSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class QuestionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
