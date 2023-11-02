"""
Definition of views.
"""

from datetime import datetime
from tkinter import NO
from django.shortcuts import render
from django.http import HttpRequest

from app.forms import AnketaForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
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
            'title':'Контакты',
            'message':'Страница с нашими контактами',
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
            'title':'О нас',
            'message':'Сведения о нас',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1':'Мужчина','2':'Женщина'}
    internet = {'1':'Каждый день','2':'Несколько раз в день','3':'несколько раз в неделю','4':'Несколько раз в месяц'}
    
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['internet'] = internet[form.cleaned_data['internet']]
            if form.cleaned_data['notice'] == True:
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
        else:
            form = AnketaForm()
        return render(request,'app/anketa.html',
                      {'form':form,
                       'data': data}
                      )
