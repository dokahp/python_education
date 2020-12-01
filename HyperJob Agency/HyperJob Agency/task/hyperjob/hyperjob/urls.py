"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from mainpage.views import MainPage, Login, SignUp, PrivateOffice
from resume.views import ResumeHome, AddResume
from vacancy.views import VacancyHome, AddVacancy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='MainPage'),
    path('resumes', ResumeHome.as_view()),
    path('vacancies', VacancyHome.as_view()),
    path('login', Login.as_view()),
    path('signup', SignUp.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home', PrivateOffice.as_view()),
    path('resume/new', AddResume),
    path('vacancy/new', AddVacancy)

]
