from django.urls import path
from .views import HomePageView, PasswordCreateView, PasswordListView, PasswordDeleteView, PasswordUpdateView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("new/",PasswordCreateView.as_view(), name="password_new" ),
    path("list/", PasswordListView.as_view(), name="password_list"),
    path("<int:pk>/delete/", PasswordDeleteView.as_view(), name="password_delete"),
    path("<int:pk>/edit", PasswordUpdateView.as_view(), name="password_edit"),
]