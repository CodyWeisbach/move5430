# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Completed views
def index(request):
	return render(request, "index.html")

def cody(request):
	return render(request, "cody.html")

def thanks(request):
	context = {
	"type": "about"
	}
	return render(request, "thanks.html", context)

def letters(request):
	context = {
	"title": "Letters",
	"type": "about"
	}
	return render(request, "letters.html", context)

def contact(request):
	context = {
	"title": "Contact"
	}
	return render(request, "contact.html", context)

def mop(request):
	context = {
	"title": "Choose Movement Over Pain"
	}
	return render(request, "mop.html", context)

# Priority to launch	





def codynow(request):
	return HttpResponse("this is the cody now page")

def cara(request):
	return HttpResponse("this is the cara main page")

def caranow(request):
	return HttpResponse("this is the cara now page")


# Next tier priority

def about(request):
	return HttpResponse("this is the long about page")

def aboutcody(request):
	return HttpResponse("this is the long about cody page")

def plans(request):
	return HttpResponse("this is the plans page")

def aboutcara(request):
	return HttpResponse("this is the long about cara page")




