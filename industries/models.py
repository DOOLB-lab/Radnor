from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.utils.timezone import now

class Service(models.Model):
    TYPE_CHOICES = [
        ('industry', 'Industry'),
        ('capability', 'Capability'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    banner_title = models.CharField(max_length=200)
    banner_subtitle = models.TextField()
    banner_image = models.ImageField(upload_to='banners/')
    content = CKEditor5Field('Content', config_name='default')

    def __str__(self):
        return f"{self.service.name} page"

class Card(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    

    def __str__(self):
        return self.title

class WhatWeDo(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class InsightCategory(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="categories", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.service.name if self.service else 'No Service'})"

class OurInsights(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='insights/', blank=True, null=True)
    category = models.ForeignKey(InsightCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='insights')
    published_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} ({self.get_service()})"

    def get_service(self):
        return self.category.service.name if self.category and self.category.service else "No Service"
    get_service.short_description = "Service"