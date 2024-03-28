"""
URL configuration for eventproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]





# djangoproject/urls.py (or similar)

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventapp.views import EventViewSet

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # <-- make sure you have this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




