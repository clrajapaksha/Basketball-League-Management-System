"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from teams import views as team_views

urlpatterns = [
    # ADMIN SITE
    path('admin/', admin.site.urls),

    # API ENDPOINTS
    path('api/v1/teams/', team_views.TeamList.as_view()),
    path('api/v1/teams/<int:team_id>/', team_views.TeamDetail.as_view()),
    path('api/v1/teams/<int:team_id>/players/', team_views.PlayerList.as_view()),
    path('api/v1/teams/<int:team_id>/players/<int:player_id>/', team_views.PlayerDetail.as_view()),

    # SCHEMA
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
