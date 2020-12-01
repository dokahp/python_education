from django.shortcuts import render
from django.views import View
from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User


# Create your views here.
class MainPage(View):
    def get(self, request):
        return render(request, 'hyperjob/index.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'hyperjob/signup.html'


class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class PrivateOffice(View):
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            form = User.objects.filter(username=username)
            return render(request, 'hyperjob/privateoffice.html', {'form': form})
        # более логичное поведение, раскомментируем и удаляем последнюю строку
        # else:
        #     return HttpResponseForbidden('You need log in to use private office')
        return render(request, 'hyperjob/privateoffice.html')
