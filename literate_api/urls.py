from django.urls import include, path
from questions import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name="questions"),
    path('approved-questions/', views.FilteredQuestionList.as_view()),
    path('approve-question/<int:pk>', views.UpdateQuestionView.as_view()),
    path('create-questions/', views.QuestionView.as_view(), name="create-questions"),

    path('jokes/', views.JokeList.as_view(), name="jokes"),
    path('approved-jokes/', views.FilteredJokeList.as_view()),
    path('approve-jokes/<int:pk>', views.UpdateJokeView.as_view()),
    path('create-jokes/', views.JokeView.as_view(), name="create-jokes"),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]