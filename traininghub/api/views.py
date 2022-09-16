from http.client import HTTPResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import TrainingForm, TopicForm
from api.serializer import UserSerializer
from .serializer import TrainingSerializer, UserSerializer
from .models import Training, Topic
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()


# Create your views here.


class TrainingNew(APIView):
    def get(self, request):
        if request.method == 'POST':
            form = TrainingForm(request.POST)
            if form.is_valid():
                training = form.save()
                return redirect('training_list')
        else:
            form = TrainingForm()
        return render(request, 'api/training_form.html', {'form':form})

class TopicNew(APIView):
    def get(self, request):
        if request.method == 'POST':
            form = TopicForm(request.POST)
            if form.is_valid():
                training = form.save()
                return redirect('training_list')
        else:
            form = TopicForm()
        return render(request, 'api/topic_form.html', {'form':form})



# def training_list(request):
#     training = Training.objects.all()
#     serializer = TrainingSerializer(training, many=True)
#     return Response(serializer.data)

class TrainingView(APIView):
    def get(self, request):
        training = Training.objects.all()
        serializer = TrainingSerializer(training, many=True)
        return Response(serializer.data)


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