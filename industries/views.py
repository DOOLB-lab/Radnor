from django.shortcuts import render, get_object_or_404
from .models import Service, Page, Card, WhatWeDo, InsightCategory, OurInsights, InsightCategory

def home_page(request):
    # Fetch services for dropdown
    industries = Service.objects.filter(type='industry')
    capabilities = Service.objects.filter(type='capability')

    # Fetch latest capability insight (most recent published_date)
    latest_insight = (
        OurInsights.objects
        .filter(page__service__type='capability')
        .order_by('-published_date')
        .first()
    )

    # Fetch older capability insights (excluding the latest)
    older_insights = (
        OurInsights.objects
        .filter(page__service__type='capability')
        .exclude(id=latest_insight.id if latest_insight else None)
        .order_by('-published_date')[:3]  # Limit to 3 older insights
    )

    context = {
        'industries': industries,
        'capabilities': capabilities,
        'latest_insight': latest_insight,
        'older_insights': older_insights,
    }
    return render(request, 'services/home.html', context)

def how_we_help_clients(request, service_slug, service_type):
    # Fetch the service (industry or capability) based on the slug
    service = get_object_or_404(Service, slug=service_slug, type=service_type)
    
    # Fetch the page and related data
    page = get_object_or_404(Page, service=service)
    cards = Card.objects.filter(page=page)
    what_we_do = WhatWeDo.objects.filter(page=page)
    
    context = {
        'service': service,
        'page': page,
        'cards': cards,
        'what_we_do': what_we_do,
    }
    return render(request, 'services/how_we_help_clients.html', context)

def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    
    # Fetch all services for the dropdown
    industries = Service.objects.filter(type='industry')
    capabilities = Service.objects.filter(type='capability')

    context = {
        'card': card,
        'industries': industries,
        'capabilities': capabilities,
    }
    return render(request, 'services/card_detail.html', context)

def our_insights(request, service_slug, service_type):
    # Fetch the service (industry or capability) based on the slug and type
    service = get_object_or_404(Service, slug=service_slug, type=service_type)
    
    # Fetch the page and related data
    page = get_object_or_404(Page, service=service)
    insights = OurInsights.objects.filter(page=page)
    categories = InsightCategory.objects.filter(insights__page=page).distinct()

    context = {
        'service': service,
        'page': page,
        'insights': insights,
        'categories': categories,
        'service_slug': service_slug,
    }
    return render(request, 'services/our_insights.html', context)

def insight_detail(request, service_slug, insight_id, service_type):
    # Fetch the service (industry or capability) based on the slug and type
    service = get_object_or_404(Service, slug=service_slug, type=service_type)
    page = get_object_or_404(Page, service=service)
    # Fetch the insight
    insight = get_object_or_404(OurInsights, id=insight_id, page__service=service)

    context = {
        'service': service,
        'insight': insight,
        'page': page,
    }
    return render(request, 'services/insight_detail.html', context)

def featured_insights(request, category_id):
    # Fetch the selected category and its insights
    category = get_object_or_404(InsightCategory, id=category_id)

    # Fetch all categories for the Featured Insights dropdown
    featured_categories = InsightCategory.objects.filter(service__type='capability')

    context = {
        'category': category,
        'featured_categories': featured_categories,  # Add this line
    }
    return render(request, 'services/featured_insights.html', context)