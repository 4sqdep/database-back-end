from django.urls import path
from .views import RegistrationAPIView, LoginView


app_name = "account"

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name="register"),

    path('login/', LoginView.as_view(), name="login")
]