from django.shortcuts import render, redirect
from homepage.models import Insight  # Import your model
from .forms import InsightForm  # We'll create this form next

def dashboard(request):
    insights = Insight.objects.all()
    return render(request, 'custom_admin/dashboard.html', {'insights': insights})

def add_insight(request):
    if request.method == "POST":
        form = InsightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InsightForm()
    return render(request, 'custom_admin/add_insight.html', {'form': form})

