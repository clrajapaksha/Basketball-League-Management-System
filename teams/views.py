from rest_framework import generics, mixins
from teams.models import Team, Player
from teams.serializers import TeamSerializer, PlayerSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # #@extend_schema(request=TaskCreationSerializer, responses={201: TaskSerializer}, methods=["POST"])
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url_kwarg = 'team_id'


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class BestPlayerList(generics.ListAPIView):
    #queryset = Player.objects.annotate(avg_score=).order_by('avg_score')
    pass


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_url_kwarg = 'player_id'
