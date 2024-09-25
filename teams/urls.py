from django.urls import path
from teams.views import TeamView, TeamDetailedView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamDetailedView.as_view()),
]
