from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrCoach
from teams.models import Team, Player
from teams.serializers import TeamSerializer, PlayerSerializer


class TeamList(generics.ListCreateAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCoach]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # #@extend_schema(request=TaskCreationSerializer, responses={201: TaskSerializer}, methods=["POST"])
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCoach]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url_kwarg = 'team_id'


class PlayerList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCoach]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class BestPlayerList(generics.ListAPIView):
    #queryset = Player.objects.annotate(avg_score=).order_by('avg_score')
    pass


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCoach]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_url_kwarg = 'player_id'
