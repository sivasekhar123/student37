# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class StudentApps(models.Model):
    """
    to create StudentApps table
    """
    email = models.EmailField()
    name = models.CharField(max_length=30)
    ssc = models.ImageField(upload_to='images')
    inter = models.ImageField(upload_to='images')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    to create Department table
    """
    mechanical = 'M.E'
    civil = 'C.E'
    electrical = 'E.E.E'
    electronics = 'E.C.E'
    computer = 'C.S.E'
    department_choices = (
        (mechanical, 'Mechanical'),
        (civil, 'Civil'),
        (electrical, 'Electrical'),
        (electronics, 'Electronics'),
        (computer, 'Computer')
    )
    department = models.CharField(max_length=20, choices=department_choices, default=mechanical)

    def __str__(self):
        return self.department


class StudentReg(models.Model):
    """
    to create StudentReg table
    """
    student_apps = models.OneToOneField(StudentApps)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    father = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    user = models.OneToOneField(User)
    department = models.ForeignKey(Department)
    profile_pic = models.ImageField(upload_to='images')
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StaffReg(models.Model):
    """
    to create StaffReg table
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    department = models.ForeignKey(Department)
    qualification = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images')
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.name
