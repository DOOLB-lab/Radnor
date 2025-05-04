# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home_page, name='home'),

    # Industries URLs
    path('industries/<str:service_slug>/how-we-help-clients/', views.how_we_help_clients, {'service_type': 'industry'}, name='industry_how_we_help_clients'),
    path('industries/<str:service_slug>/our-insights/', views.our_insights, {'service_type': 'industry'}, name='industry_our_insights'),
    path('industries/<str:service_slug>/insight/<int:insight_id>/', views.insight_detail, {'service_type': 'industry'}, name='industry_insight_detail'),

    # Capabilities URLs
    path('capabilities/<str:service_slug>/how-we-help-clients/', views.how_we_help_clients, {'service_type': 'capability'}, name='capability_how_we_help_clients'),
    path('capabilities/<str:service_slug>/our-insights/', views.our_insights, {'service_type': 'capability'}, name='capability_our_insights'),
    path('capabilities/<str:service_slug>/insight/<int:insight_id>/', views.insight_detail, {'service_type': 'capability'}, name='capability_insight_detail'),

    # Card detail (shared between industries and capabilities)
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    # Featured Insights
    path('featured-insights/<int:category_id>/', views.featured_insights, name='featured_insights'),
]