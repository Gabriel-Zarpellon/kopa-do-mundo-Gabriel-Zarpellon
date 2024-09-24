from rest_framework.views import APIView, status, Response, Request
from django.forms.models import model_to_dict
from teams.models import Team
from utils import (
    data_processing,
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError,
)


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        try:
            data_processing(**request.data)
        except NegativeTitlesError:
            return Response(
                {"error": "titles cannot be negative"},
                status.HTTP_400_BAD_REQUEST
            )
        except InvalidYearCupError:
            return Response(
                {"error": "there was no world cup this year"},
                status.HTTP_400_BAD_REQUEST,
            )
        except ImpossibleTitlesError:
            return Response(
                {"error": "impossible to have more titles than disputed cups"},
                status.HTTP_400_BAD_REQUEST,
            )

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams_dict = [model_to_dict(team) for team in Team.objects.all()]

        return Response(teams_dict, status.HTTP_200_OK)
