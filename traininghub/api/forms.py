from dataclasses import field, fields
from django import forms
from .models import Module, QuizQuestion, Training, Topic
from django.forms import formset_factory

TopicFormSet = formset_factory(Topic)


TrainingFormSet = formset_factory(Training)

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ("topic",)


class TrainingForm(forms.ModelForm):
    
    class Meta:
        model=Training
        fields=('title','details')
        

        
class ModuleForm(forms.ModelForm):
    
    class Meta:
        model = Module
        fields=('title','training')
        
        
class QuizQuestionsForm(forms.ModelForm):
    
    class Meta:
        model=QuizQuestion
        fields=('question','option1','option1','option3','option4','answer')