from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Page


# ✅ Form to use CKEditor in the Admin Panel
class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))   # ✅ This ensures CKEditor works

    class Meta:
        model = Page
        fields = '__all__'