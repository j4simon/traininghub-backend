from time import timezone
from django.db import models
# from taggit.managers import TaggableManager
from django.utils.timezone import now
# Create your models here.

# class User(models.Model):
#      first_name = models.CharField(max_length=50)
#      last_name = models.CharField(max_length=50)
#      employee_number = models.IntegerField()
#      company = models.CharField(max_length=50)
#      department = models.CharField(max_length=50)
#      title = models.CharField(max_length=50)
# class Topic(models.Model):
#     tags = TaggableManager
          
    # def __str__(self):
    #     return self.topic
class Topic(models.Model):
    topic = models.CharField(max_length=50)
    
    def __str__(self):
        return self.topic

class Training(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(default=now, editable=False) 
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=50)
    training = models.ManyToManyField(Training)
    created = models.DateTimeField(default=now, editable=False) 

    def __str__(self):
        return self.title   
    
    
  
class QuizQuestion(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question
    
class Quiz(models.Model):
    title = models.CharField(max_length=50, default='title')
    questions = models.ManyToManyField(QuizQuestion)
    
    def __str__(self):
        return self.title