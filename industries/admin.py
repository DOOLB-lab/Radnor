from django.contrib import admin
from .models import Service, Page, Card, WhatWeDo, OurInsights, InsightCategory

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type')
    search_fields = ('name',)
    list_filter = ('type',)  # Filter by type (industry or capability)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('service', 'banner_title', 'get_service_type')
    list_filter = ('service__type', 'service')  # Filter by service type and service
    search_fields = ('banner_title', 'banner_subtitle')

    def get_service_type(self, obj):
        return obj.service.type
    get_service_type.short_description = 'Service Type'

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'get_service_type')
    list_filter = ('page__service__type', 'page')  # Filter by service type and page
    search_fields = ('title', 'description')

    def get_service_type(self, obj):
        return obj.page.service.type
    get_service_type.short_description = 'Service Type'

@admin.register(WhatWeDo)
class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'get_service_type')
    list_filter = ('page__service__type', 'page')  # Filter by service type and page
    search_fields = ('title', 'description')

    def get_service_type(self, obj):
        return obj.page.service.type
    get_service_type.short_description = 'Service Type'

@admin.register(InsightCategory)
class InsightCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'get_service_type')  # Show category + service + type
    list_filter = ('service__type', 'service')  # Filter by service type and service
    search_fields = ('name', 'service__name')  # Allow searching by category & service name
    autocomplete_fields = ('service',)  # Faster selection when adding new categories

    def get_service_type(self, obj):
        return obj.service.type
    get_service_type.short_description = 'Service Type'

@admin.register(OurInsights)
class OurInsightsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_service', 'category', 'published_date', 'get_service_type')  # Show Service, Category, and Type
    list_filter = ('category__service__type', 'category', 'published_date')  # Filter by service type, category, and date
    search_fields = ('title', 'description', 'category__service__name')  # Search by title, description, and service name
    ordering = ('-published_date',)

    def get_service(self, obj):
        return obj.category.service.name if obj.category else "No Service"
    get_service.short_description = 'Service'

    def get_service_type(self, obj):
        return obj.category.service.type if obj.category else "No Type"
    get_service_type.short_description = 'Service Type'