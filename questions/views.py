from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, GroupSerializer, QuestionSerializer
from .models import Question


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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]