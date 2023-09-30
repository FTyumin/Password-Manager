from django.urls import path
from .views import HomePageView, NewPasswordView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("new/",NewPasswordView.as_view(), name="password_new" ),
    
]