# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)

def upload_location(instance, filename):
    return "%s/%s" %('posts', filename)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=120, blank=False, unique=True)
    slug = models.SlugField(unique=True)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True,
        upload_to=upload_location,
        height_field="height_field", 
        width_field="width_field")
    height_field = models.IntegerField(default=200)
    width_field = models.IntegerField(default=220)
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    
    objects = PostManager()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug':str(self.slug)})

    class Meta:
        ordering = ['title']

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = BlogPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists: 
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    
pre_save.connect(pre_save_post_receiver, sender=BlogPost)