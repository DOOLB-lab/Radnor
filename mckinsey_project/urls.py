from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
    # Change this line - remove 'industries/' prefix
    path('', include('industries.urls')),  # Now serves at root URL
    
    # Keep this if you want to maintain both URLs for backward compatibility
    # path('industries/', include('industries.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)