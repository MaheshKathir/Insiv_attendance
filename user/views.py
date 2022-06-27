from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, message
import math, random
import datetime
from django.contrib.auth.models import User

from user import models
from user.models import user


def home(request):
    return render(request, 'WebSite2038352/index.html')


def login(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        models.user.objects.filter(user_name=user_name, password=password)
        return render(request, 'WebSite2038352/for_attendence.html')
    else:
        return render(request, 'WebSite2038352/index.html')


def forget(request):
    return render(request, 'WebSite2038352/templates/forget.html')



def register(request):
    return render(request, 'WebSite2038352/Register.html')


def register_submit(request):
    if request.method == 'POST':
        value = user()
        value.employee_id = request.POST['employee_id']
        value.user_name = request.POST['user_name']
        value.email = request.POST['email']
        value.dob = request.POST['dob']
        value.password = request.POST['password']
        value.confirm_password = request.POST['confirm_password']
        if value.password != value.confirm_password:
            return redirect('Register')
        elif value.user_name == "" or value.password == "":
            messages.info(request, 'some fields are empty')
            return redirect('Register')
        else:
            value.save()
        return render(request, 'WebSite2038352/index.html')

