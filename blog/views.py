# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
		"type": "oneblog"
	}
	return render(request, "blog_detail.html", context)

def blog_list(request):
	queryset_list = BlogPost.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = BlogPost.objects.all()
	#query = request.GET.get('q')
	#if query:
	#	queryset_list = queryset_list.filter(
	#		Q(title__icontains=query)|
	#		Q(text__icontains=query)
	#		).distinct()
	context = {
	"title": "blog",
	"type": "content",
	"posts": queryset_list
	}
	return render(request, "blog_list.html", context)

@login_required
def blog_update(request, slug=None):
	if not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(BlogPost, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"title": "Edit" + " " + instance.title,
	"type": "Update",
	"post":instance,
	"form":form,
	}
	return render(request, "blog_form.html", context)
	
@login_required
def blog_confirm_delete(request, slug=None):
	instance = get_object_or_404(BlogPost, slug=slug)
	if instance.draft:
		if not request.user.is_staff:
			raise Http404
	context = {
		"title": instance.title,
		"post": instance,
		"type": "oneblog"
	}
	return render(request, "blog_confirm_delete.html", context)

@login_required
def blog_delete(request, slug=None):
	if not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(BlogPost, slug=slug)
	instance.delete()
	return redirect("list")




