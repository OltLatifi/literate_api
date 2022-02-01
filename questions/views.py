from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import QuestionSerializer, JokeSerializer
from .models import Question, Joke


from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    

class QuestionView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes=[AllowAny,]


class UpdateQuestionView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class FilteredQuestionList(generics.ListAPIView):
    queryset = Question.objects.filter(approved=True)
    serializer_class = QuestionSerializer



class JokeList(generics.ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    

class JokeView(generics.CreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    permission_classes=[AllowAny,]


class FilteredJokeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class FilteredJokeList(generics.ListAPIView):
    queryset = Joke.objects.filter(approved=True)
    serializer_class = JokeSerializer
