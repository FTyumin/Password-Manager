from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from .models import Password



class HomePageView(TemplateView):
    model = Password
    template_name = "home.html"


class PasswordCreateView(CreateView):
    model = Password
    template_name = "password_new.html"
    fields = ["title", "password"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PasswordUpdateView(UpdateView):
    model = Password
    template_name = "password_edit.html"
    fields = ["title", "password"]
    success_url = "/"


class PasswordDeleteView(DeleteView):
    model = Password
    template_name = "password_delete.html"
    success_url = "/"


class PasswordListView(ListView):
    model = Password
    template_name = "password_list.html"
    context_object_name = "passwords"

    def get_queryset(self):
        return Password.objects.all()
