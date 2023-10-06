from django.urls import path
from .views import ChatPage
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", ChatPage, name="chat-page"),
    path("auth/login", LoginView.as_view(template_name= "chat/LoginPage.html"), name="login-user"),
    path("auth/logout", LogoutView.as_view(), name="logout-user")
]
