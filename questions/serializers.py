from django.contrib.auth.models import User
from .models import Question, Joke
from rest_framework import serializers

from rest_framework.response import Response
from django.contrib.auth import authenticate


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = "__all__"


# jwt login
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")