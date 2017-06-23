# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Message, Comment
from ..login.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def setadmin(request):
    print "in set admin"
    user = User.objects.get(id=1)
    user.user_level = "admin"
    user.save()
    print user.user_level

def dashboard(request):
    if request.session['user_level'] == "admin":
        users = User.objects.all()
        context= {'users':users}
        return render(request, 'dashboard/admindash.html', context)
    else:
        users = User.objects.all()
        context = {'users':users}
        return render(request, 'dashboard/dashboard.html', context)

def edit(request, id):
    print "in edit"
    print type(id)
    print type(request.session['id'])
    if request.session['user_level'] == "admin" or request.session['id'] == int(id):
        print "in if statemetn"
        user = User.objects.get(id=id)
        context = {'user':user}
        return render(request, 'dashboard/showuser.html', context)
    else:
        return redirect('/dashboard')

def update(request):
    user = User.objects.update(request.POST)
    return redirect(reverse('edit', kwargs={'id':request.POST['id']}))

def password(request):
    user = User.objects.update(request.POST)
    if user['status']:
        messages.error(request, "Password successfully changed", extra_tags="changepass")
        return redirect(reverse('edit', kwargs={'id':request.POST['id']}))
    else:
        for error in user['errors']:
            messages.error(request, error, extra_tags="changepass")
        return redirect(reverse('edit', kwargs={'id':request.POST['id']}))
        

def description(request):
    user = User.objects.description(request.POST)
    return redirect(reverse('edit', kwargs={'id':request.POST['id']}))

def newuser(request):
    if request.session['user_level'] == "admin":
        return render(request, 'dashboard/newuser.html')
    else:
        return redirect('/dashboard')

def adduser(request):
    if request.session['user_level'] == "admin":
        print "in adduser"
        user = User.objects.adduser(request.POST)
        print user
        if not user['status']:
            for error in user['errors']:
                messages.error(request, error, extra_tags="register")
            return redirect ('/registration')
        else:
            print "register success"
            return redirect ('/dashboard')
    else:
        return redirect('/dashboard')

def confirm(request, id):
    context = {'id':id}
    return render(request, 'dashboard/confirm.html', context)

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/dashboard')

def show(request, id):
    user = User.objects.get(id=id)
    messages = Message.objects.filter(mess_wall=user)
    comments = Comment.objects.all()
    context={'user': user, 'messages':messages, 'comments':comments}
    return render(request,'dashboard/show.html', context)

def message(request):
    print request.session['id']
    walluser = User.objects.get(id=request.POST['wallid'])
    messuser = User.objects.get(id=request.session['id'])
    Message.objects.create(message=request.POST['message'], mess_wall=walluser, mess_creator=messuser)
    return redirect(reverse('show', kwargs={'id':request.POST['wallid']}))

def comment(request):
    mess = Message.objects.get(id=request.POST['messid'])
    commuser = User.objects.get(id=request.session['id'])
    Comment.objects.create(comment=request.POST['comment'], comm_message=mess, comm_user=commuser)
    return redirect(reverse('show', kwargs={'id':request.POST['wallid']}))

def logout(request):
    request.session['id'] = None
    request.session['user_status'] = None
    return redirect('/login')
