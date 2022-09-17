from django.contrib import admin
from .models import Training, Topic, Module, QuizQuestion, Quiz

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title','detail','created','topics')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title','training','created')

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question','option1','option2','option3','option4','answer')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title','questions')
    
# Register your models here.
admin.site.register(Training)
admin.site.register(Topic)
admin.site.register(Module)
admin.site.register(QuizQuestion)
admin.site.register(Quiz)