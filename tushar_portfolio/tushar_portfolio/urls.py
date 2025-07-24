from django.contrib import admin
from django.urls import path, include


print("THIS IS MY URLS.PY 00")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path('resume/', include('resume.urls')),
    path('contact/', include('contact.urls')),
    path('core/', include('core.urls')),
]