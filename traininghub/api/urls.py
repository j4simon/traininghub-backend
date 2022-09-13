from django.urls import path
from . import views

urlpatterns = [
    # path('cats-list/', views.cats_list, name="cats_list"),
    path('training-list/', views.TrainingView.as_view(), name='training_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('training/new', views.training_new, name='training_new'),

]
