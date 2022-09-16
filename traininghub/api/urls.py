from django.urls import path
from . import views

urlpatterns = [
    path('api/training-list/', views.TrainingView.as_view(), name='training_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/training/new/', views.TrainingNew.as_view(), name='training_new'),
    path('api/topic/new', views.TopicNew.as_view(), name='topic_new')
]
