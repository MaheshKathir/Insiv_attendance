from django.db import models


# Create your models here.
class user(models.Model):
    employee_id = models.CharField(max_length=100, default=0)
    user_name = models.CharField(max_length=100, default=0)
    email = models.CharField(max_length=100, default=0)
    dob = models.CharField(max_length=100, default=0)
    password = models.CharField(max_length=100, default=0)
    confirm_password = models.CharField(max_length=100, default=0)
    clock_in = models.CharField(max_length=100, default=0)
    clock_out = models.TimeField(auto_now=True)
    # ontime_in = models.TimeField(auto_now=False)
    # ontime_out = models.TimeField(auto_now=False)
