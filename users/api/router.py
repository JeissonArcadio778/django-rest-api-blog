from django.urls import path 
from users.api.views import RegisterUserView


urlpatterns = [
    path('auth/register', RegisterUserView.as_view()),
]