from django.urls import path
from .views import RegistrationAPIView, LoginView, UserProfileAPIView


app_name = "account"

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name="register"),

    path('login/', LoginView.as_view(), name="login"),

    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='profile')
]