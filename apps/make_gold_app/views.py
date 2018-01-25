# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'gold' : request.session['gold'] 
        }
    return render(request, 'make_gold_app/index.html', context)

def process(request):
    this_gold = 0
    action = 'earned'
    if request.POST['place'] == 'farm':
        request.session['gold'] += random.randint(10, 20)
    if request.POST['place'] == 'cave':
        request.session['gold'] += random.randint(5, 10)
    if request.POST['place'] == 'house':
        request.session['gold'] += random.randint(2, 5)
    if request.POST['place'] == 'casino':
        request.session['gold'] += random.randint(-50, 50)
    return redirect('/')
    
def reset(request):
    del request.session['gold']
    return redirect('/')
    