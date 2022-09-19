from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'training',views.TrainingView,basename='training')
# router.register(r'training-list',views.TrainingView,basename='training')
router.register(r'topic',views.TopicNew,basename='topic')
router.register(r'quiz-question',views.QuizQuestion,basename='quizQuestion')
router.register(r'quiz',views.Quiz,basename='quiz')
router.register(r'module',views.Module,basename='module')



# urlpatterns = [
#     path('register/', views.RegisterView.as_view(), name='register'),
#     path('login/', views.LoginView.as_view(), name='login'),
#     # path('api/training/new/', views.TrainingNew.as_view(), name='training_new'),
#     # path('api/topic/new/', views.TopicNew.as_view(), name='topic_new')
# ]
# urlpatterns += router.urls
urlpatterns = router.urls