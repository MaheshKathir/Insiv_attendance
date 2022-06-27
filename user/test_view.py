from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
import datetime
import time

from user import models
from user.models import user


def home(request):
    return render(request, 'WebSite2038352/index.html')


def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.user.objects.authenticate(username=username, password=password)
        if user is not None:
            login(request)
            return redirect("/")
        else:
            msg = 'Invalid credentials'

    # return render(request, 'WebSite2038352/login.html')
    clock_in = datetime.datetime.now()
    add_clock_in = models.user.objects.create(clock_in=clock_in)
    add_clock_in.save()

    clock_out = datetime.datetime.now()
    duration = clock_out - clock_in

    add_clock_get = models.user.objects.all()
    return render(request, 'WebSite2038352/for_attendence.html', {'clock_in': clock_in, 'clock_out': clock_out,
                                                                  'duration': duration})

    # return render(request, 'WebSite2038352/for_attendence.html')


def forget(request):
    return render(request, 'WebSite2038352/templates/forget.html')


def register(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = models.user.objects.create(employee_id=employee_id, user_name=user_name, email=email, dob=dob,
                                          password=password,
                                          confirm_password=confirm_password)
    #     if user.is_valid():
        user.save()
    #         messages.success(request, f'Your Account has been Ready.You can log in now!')
        return redirect('WebSite2038352/index.html')
    #     else:
    #         return render(request, 'WebSite2038352/Register.html')

    # msg = None
    # success = False
    #
    # if request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get("username")
    #         raw_password = form.cleaned_data.get("password1")
    #         user = authenticate(username=username, password=raw_password)
    #
    #         msg = 'User created - please <a href="/login">login</a>.'
    #         success = True
    #
    #
    #         # return redirect("/login/")
    #
    #     else:
    #         msg = 'Form is not valid'
    # else:
    #     form = SignUpForm()
    #
    # return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

    # employee_id = request.POST.get('employee_id')
    # user_name = request.POST.get('user_name')
    # email = request.POST.get('email')
    # dob = request.POST.get('dob')

    # password = request.POST.get('password')
    # confirm_password = request.POST.get('confirm_password')
    # value = models.user.objects.create(employee_id=employee_id, user_name=user_name, email=email, dob=dob,
    #
    #                                        password=password, confirm_password=confirm_password)
    # value.save()
    # messages.success(request, f'Your Account has been Ready.You can log in now!')

    # return render(request, 'WebSite2038352/index.html')


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
        print(OTP)
    return OTP


def send_otp(request):
    email = request.POST.get("email")
    o = generateOTP()
    htmlgen = '<p>Your OTP is <strong>' + o + '</strong></p>'
    send_mail('OTP request', o, '<gmail id>', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)


def clock_in(request):
    # onTime_in = datetime.datetime.now().time()
    clock_in = datetime.datetime.now()
    add_clock_in = models.user.objects.create(clock_in=clock_in)
    add_clock_in.save()

    return render(request, 'WebSite2038352/for_attendence.html', {'add_clock_in': add_clock_in})

# def clock_out(request):
#     onTime_in = datetime.datetime.now().time()
#     ontTime_out = datetime.datetime.now().time()
#
#     clock_in = datetime.datetime.now()
#
#     clock_out = datetime.datetime.now()
#     duration = clock_out - clock_in
#     return render(request, 'WebSite2038352/for_attendence.html', {'duration': duration})
