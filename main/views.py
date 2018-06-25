# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html")

def about(request):
	return HttpResponse("this is the long about page")

def plans(request):
	return HttpResponse("this is the plans page")

def cody(request):
	return HttpResponse("this is the cody main page")

def aboutcody(request):
	return HttpResponse("this is the long about cody page")

def codynow(request):
	return HttpResponse("this is the cody now page")

def cara(request):
	return HttpResponse("this is the cara main page")

def aboutcara(request):
	return HttpResponse("this is the long about cara page")

def caranow(request):
	return HttpResponse("this is the cara now page")

def letters(request):
	return HttpResponse("this is the letters page")