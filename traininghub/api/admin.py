from django.contrib import admin
from .models import Training

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title','description','category', 'training_link')
    
# Register your models here.
admin.site.register(Training)