from django.urls import include, path
from rest_framework import routers
from questions import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing. 
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('questions/', views.QuestionList.as_view(), name="questions"),
    path('approved-questions/', views.FilteredQuestionList.as_view()),
    path('approve-question/<int:pk>', views.UpdateQuestionView.as_view()),
    path('create-questions/', views.QuestionView.as_view(), name="create-questions"),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]