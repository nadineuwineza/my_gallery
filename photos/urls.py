from django.urls import path
from photos import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photos'

urlpatterns = [
    path('', views.index),
    path('location/<str:location_name>', views.image_location,name='location'),
    path('search/', views.search_results,name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)