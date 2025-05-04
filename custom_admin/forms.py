from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from homepage.models import Insight  # Import the model where CKEditor should be used

class InsightForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))  # ✅ Enable CKEditor in form

    class Meta:
        model = Insight
        fields = '__all__'  # Use all fields from the model
