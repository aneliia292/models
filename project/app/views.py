from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from .models import *


def posts(request):
    post = Posts.objects.all()
    return render(request, 'forum.html', context={'post': post})



# def index(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             password = form.cleaned_data['password']
#             email = form.cleaned_data['email']
#             return HttpResponse(
#                 f'<h1>{name}, поздравляю с регистрацией! <br>Данные: name - {name}, password - {password}, Email - {email}</h1>')
#         else:
#             return HttpResponse('Данные не валидны')
#     else:
#         form = UserForm()
#         return render(request, 'index.html', context={'form': form})
