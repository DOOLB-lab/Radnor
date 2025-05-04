from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Page  # Import the model where CKEditor should be used

class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))  # ✅ Enable CKEditor in form

    class Meta:
        model = Page
        fields = '__all__'  # Use all fields from the model
