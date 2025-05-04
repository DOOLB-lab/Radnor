from .models import Service, InsightCategory

def services(request):
    # Fetch all industries and capabilities
    industries = Service.objects.filter(type='industry')
    capabilities = Service.objects.filter(type='capability')
    
    return {
        'industries': industries,  # Pass industries to the template
        'capabilities': capabilities,  # Pass capabilities to the template
    }


def featured_categories_processor(request):
    featured_categories = InsightCategory.objects.filter(service__type='capability')
    return {'featured_categories': featured_categories}
