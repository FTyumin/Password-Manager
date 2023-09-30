from django.urls import path
from .views import HomePageView, PasswordCreateView, PasswordListView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("new/",PasswordCreateView.as_view(), name="password_new" ),
    path("list/", PasswordListView.as_view(), name="password_list"),
    
]