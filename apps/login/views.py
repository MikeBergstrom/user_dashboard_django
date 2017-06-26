# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import datetime


def index(request):

    # User.objects.all().delete()
    # print User.objects.all()

    return render(request, 'login/login.html')

def login(request):
    return render(request, 'login/login.html')

def logprocess(request):
    print "in logprocess"
    print request.POST
    user= User.objects.login(request.POST)
    if user['status']:
        request.session['first'] = user['user'].first_name
        request.session['id'] = user['user'].id
        request.session['user_level'] = user['user'].user_level
        request.session['status'] = "logged in"
        return redirect('/dashboard')
    else:
        for error in user['errors']:
            messages.error(request, error, extra_tags="login")
        return redirect('/')

def registration(request):
    return render(request, 'login/register.html')

def register(request):
    print "in register"
    user = User.objects.register(request.POST)
    print user
    if not user['status']:
        for error in user['errors']:
            messages.error(request, error, extra_tags="register")
        return redirect ('/registration')
    else:
        print "register success"
        print user['user'].first_name
        request.session['first'] = user['user'].first_name
        request.session['id'] = user['user'].id
        request.session['user_level'] = user['user'].user_level
        print request.session['first']
        print request.session['id']
        return redirect ('/dashboard')    
