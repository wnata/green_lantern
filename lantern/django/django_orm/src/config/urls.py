"""car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from apps.newsletter.views import NewsLeterViews
from common.views import LoginView, logout_view
from apps.cars.views import CarList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', TemplateView.as_view(template_name='success_url.html'), name = 'success'),
    path('newsleter/', NewsLeterViews.as_view(), name='newsletter'),
    path('car/', CarList.as_view(), name='car_list_url' ),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)