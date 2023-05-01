"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from app.forms import StudentLogin
from slcm.models import Registration

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def login(request):
    ip = StudentLogin()

    return render(request, 'app/login.html', {"form": ip})

def portfolio(request):
    data = Registration.objects.values('reg_no')
    regs = [i['reg_no'] for i in data]

    myform = StudentLogin(request.POST)
    if myform.is_valid():
        reg = myform.cleaned_data['reg_no']
        paswd = myform.cleaned_data['pswd']

        if reg in regs:
            if paswd == Registration.objects.get(reg_no = reg).password:
                student = Registration.objects.get(reg_no = reg)
                return render(request, 'app/portfolio.html', {"student": student})
            else:
                messages.error(request, 'Invalid Username')
                return redirect('studentlogin')
        else:
            messages.error(request, 'Invalid Username')
            return redirect('studentlogin')
    