from django.urls import path
from .views import dashboard, add_insight

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('add-insight/', add_insight, name='add_insight'),
]
