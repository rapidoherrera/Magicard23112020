from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from MainApp import urls


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/registro'
    template_name = 'signup.html'