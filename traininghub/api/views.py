from http.client import HTTPResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission

from .forms import TopicForm
from api.serializer import UserSerializer
from .serializer import TrainingSerializer, UserSerializer, TopicSerializer, QuizQuestionSerializer, QuizSerializer, ModuleSerializer
from .models import Training, Topic, QuizQuestion, Quiz, Module
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from api import serializer
User = get_user_model()


# Create your views here.
    

class TrainingView(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    
    def get(self,request):
        response = request.get('http://api/training_list.com')
        return render(request, 'training_list.html', {'response' : response})

class TrainingNew(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()

class TopicNew(viewsets.ModelViewSet):
        serializer_class = TopicSerializer
        queryset = Topic.objects.all()

class QuizQuestion(viewsets.ModelViewSet):
        serializer_class = QuizQuestionSerializer
        queryset = QuizQuestion.objects.all()

class Quiz(viewsets.ModelViewSet):
        serializer_class = QuizSerializer
        queryset = Quiz.objects.all()

class Module(viewsets.ModelViewSet):
        serializer_class = ModuleSerializer
        queryset = Module.objects.all()

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})