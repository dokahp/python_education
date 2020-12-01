from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from .forms import NewResume
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# Create your views here.
class ResumeHome(View):
    def get(self, request):
        resume = Resume.objects.all()
        return render(request, 'hyperjob/resume.html', {'resume': resume})


def AddResume(request):
    if request.method == 'POST':
        form = NewResume(request.POST)
        if form.is_valid():
            user = request.user.username
            author = User.objects.get(username=user)
            description = request.POST['description']
            if author.is_staff is False:
                Resume.objects.create(author=author, description=description)
                return redirect('/home')
            else:
                return HttpResponseForbidden('Forbidden')


    else:
        form = NewResume()
    return render(request, 'hyperjob/newresume.html', {'form': form})
