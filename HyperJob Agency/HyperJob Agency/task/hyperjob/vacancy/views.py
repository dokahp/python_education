from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from .forms import NewVacancy
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# Create your views here.
class VacancyHome(View):
    def get(self, request):
        vacancy = Vacancy.objects.all()
        return render(request, 'hyperjob/vacancy.html', {'vacancy': vacancy})


def AddVacancy(request):
    if request.method == 'POST':
        form = NewVacancy(request.POST)
        if form.is_valid():
            user = request.user.username
            author = User.objects.get(username=user)
            description = request.POST['description']
            if author.is_staff is True:
                Vacancy.objects.create(author=author, description=description)
                return redirect('/home')
            else:
                return HttpResponseForbidden('Forbidden')


    else:
        form = NewVacancy()
    return render(request, 'hyperjob/newvacancy.html', {'form': form})
