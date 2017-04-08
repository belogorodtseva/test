import datetime
from django.shortcuts import render, render_to_response
from appointment.forms import AddDateForm,AddTimeForm,ChooseAppForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from appointment.models import Date,Time
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'home.html')

def chooseapp(request):
    if request.method == "POST":
        form = ChooseAppForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('home')
    else:
        form = ChooseAppForm()
    return render(request, 'chooseapp.html', {'form': form})



@login_required(login_url='/login/')
def addapp(request):
    if request.method == "POST":
        formdate = AddDateForm(request.POST)
        formtime = AddTimeForm(request.POST)
        if formdate.is_valid() :
            a = formdate.save(commit=False)
            if formtime.is_valid() :
                b = formtime.save(commit=False)
                a.save()
                b.save()
                return redirect('home')

    else:
        formdate = AddDateForm()
        formtime = AddTimeForm()
    return render(request, 'addapp.html', {'formdate': formdate, 'formtime': formtime })
