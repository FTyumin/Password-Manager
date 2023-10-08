from django.urls import path
from .views import HomePageView, PasswordCreateView, PasswordListView, PasswordDeleteView, PasswordUpdateView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("password/new/",PasswordCreateView.as_view(), name="password_new" ),
    path("password/list/", PasswordListView.as_view(), name="password_list"),
    path("delete/", PasswordDeleteView.as_view(), name="password_delete"),
    path("password/<int:pk>/edit", PasswordUpdateView.as_view(), name="password_edit"),
]