from cgitb import lookup
from dataclasses import fields
from socketserver import ThreadingUnixDatagramServer
from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from api.models import Training, Module,Topic, Quiz, QuizQuestion
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
        
        
class TrainingSerializer(serializers.ModelSerializer):
    # trainingurl= serializers.HyperlinkedIdentityField(view_name="training")
    
    def get(self,request):
        response = request.get('http://api/training_list.com')
        return render(request, 'training_list.html', {'response' : response})
    
    class Meta:
        model =  Training
        fields = '__all__'
        
class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Module
        fields = '__all__'
        
class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Topic
        fields = '__all__'
        
class QuizQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  QuizQuestion
        fields = '__all__'
        
class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Quiz
        fields = '__all__'