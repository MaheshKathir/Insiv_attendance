from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
import datetime

from user import models


def home(request):
    return render(request, 'WebSite2038352/index.html')


def login(request):
    return render(request, 'WebSite2038352/for_attendence.html')


def forget(request):
    return render(request, 'WebSite2038352/templates/forget.html')


# def register(request):
#     return render(request,'WebSite2038352/Register.html')
