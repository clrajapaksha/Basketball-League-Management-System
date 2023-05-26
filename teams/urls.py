from rest_framework.routers import DefaultRouter
from django.urls import path, include

from teams import views


urlpatterns = [
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:team_id>/', views.TeamDetail.as_view()),
    path('teams/<int:team_id>/players/', views.PlayerList.as_view()),
    path('teams/<int:team_id>/players/<int:player_id>/', views.PlayerDetail.as_view()),
]