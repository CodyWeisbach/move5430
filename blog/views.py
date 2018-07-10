# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from.models import BlogPost

@login_required
def blog_create(request):
	form = BlogForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	title = "add a new post"
	context = {
		"title":title,
		"type":"Add",
		"form":form,
	}
	return render(request, "blog_form.html", context)

def blog_detail(request, slug=None):
	instance = get_object_or_404(BlogPost, slug=slug)
	if instance.draft:
		if not request.user.is_staff:
			raise Http404
	context = {
		"title": instance.title,
		"post": instance,
	}
	return render(request, "blog_detail.html", context)

def blog_list(request):
	return HttpResponse("here's the blog list page")

@login_required
def blog_update(request):
	return HttpResponse("here's where I can edit a post")

@login_required
def blog_delete(request):
	return HttpResponse("here's where I can delete a post")




