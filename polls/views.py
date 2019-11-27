# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'polls/index.html')


def detail(request):
    if request.method == 'POST':
        # import ipdb;ipdb.set_trace()
        StudentApps.objects.create(
                           name=request.POST['name'],
                           email=request.POST['email'],
                           ssc=request.FILES['ssc'],
                           inter=request.FILES['inter'],
                           )
        return redirect('polls:index')
    return render(request, 'polls/detail.html', {})


def registration(request):
    if request.method == "POST":
        email = request.POST['email']
        student_app = StudentApps.objects.get(email=email, is_verified=True)
        # if request.method == 'POST':
        # import ipdb; ipdb.set_trace()
        user = User.objects.create_user(
               username=request.POST['username'],
               email=request.POST['email'],
               password=request.POST['pwd']
                )
        department = Department.objects.create(department=request.POST['department'])
        if student_app.email == user.email:
            StudentReg.objects.create(
                student_apps=student_app,
                name=request.POST['name'],
                email=request.POST['email'],
                dob=request.POST['dob'],
                father=request.POST['father'],
                mother=request.POST['mother'],
                gender=request.POST['gender'],
                user=user,
                department=department,
                profile_pic=request.FILES['profile_pic']
            )
        return redirect('polls:index')
    return render(request, 'polls/registration.html', {})


def staff_reg(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['pwd']
        )
        department = Department.objects.create(department=request.POST['department'])
        StaffReg.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            user=user,
            department=department,
            qualification=request.POST['qualification'],
            profile_pic=request.FILES['profile_pic']
        )
        return redirect('polls:index')
    return render(request, 'polls/staff_reg.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            login(request, user)
            if hasattr(user, 'studentreg'):
                return redirect('polls:student_detail')
            elif hasattr(user, 'staffreg'):
                return redirect('polls:staff_detail')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'polls/login.html')


def logout_view(request):
    """ logging out the user from the session"""
    logout(request)
    return redirect('polls:login')


def student_detail(request):
    student = StudentReg.objects.get(user=request.user)
    context = {'student': student}
    return render(request, 'polls/student_detail.html', context)


def staff_detail(request):
    staff = StaffReg.objects.get(user=request.user)
    context = {'staff': staff}
    return render(request, 'polls/staff_detail.html', context)


def staff_info(request):
    # import ipdb;ipdb.set_trace()
    d = request.user
    e = d.studentreg.department
    staff_list = StaffReg.objects.filter(department=e)
    return render(request, 'polls/staff_info.html', {'staff_list': staff_list})


def all_students(request):
    stu_list = StudentReg.objects.all()
    return render(request, 'polls/all_students.html', {'stu_list': stu_list})


def student_info(request):
    b= request.user.staffreg.department
    student_list = StudentReg.objects.filter(department=b)
    return render(request, 'polls/student_info.html', {'student_list': student_list})


def all_staff(request):
    stf = StaffReg.objects.all()
    return render(request, 'polls/all_staff.html', {'stf': stf})
