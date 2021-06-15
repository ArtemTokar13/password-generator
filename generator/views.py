import random
import time
from django.shortcuts import render
from django.http import request, HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        characters.extend('~!@#$%^&*_+":?.,')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    length = int(request.GET.get('length', 10))
                                        # Length from home.html select. Take the 'name' of tag in html-file. end value
                                        # from selected tags
    ourpass = ''
    for char in range(length):
        ourpass += random.choice(characters)

    return render(request, 'generator/password.html', context={'password': ourpass})


def about(request):
    now = 'time to sleep'

    return render(request, 'generator/about.html', context={'time': now})
