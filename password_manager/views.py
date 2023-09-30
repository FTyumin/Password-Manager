from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from .models import Password

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class NewPasswordView(CreateView):
    model = Password
    template_name = "new_password.html"
    fields = ["title", "username", "body"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class DeletePassword(DeleteView):
    model = Password
    template_name = "delete_password.html"
    success_url = "/"

    
class PasswordListView(ListView):
    model = Password
    template_name = "password_list.html"
    context_object_name = "passwords"

    def get_queryset(self):
        return Password.objects.filter(user=self.request.user)