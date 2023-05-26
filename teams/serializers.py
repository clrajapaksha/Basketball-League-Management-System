from rest_framework import serializers
from teams.models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    #avg_score = serializers.Field(source='avg_score')
    avg_score = serializers.SerializerMethodField('get_avg_score')

    def get_avg_score(self, obj) -> float:
        return obj.total_score/obj.total_games

    class Meta:
        model = Player
        fields = ['id', 'first-name', 'last-name', 'height', 'player-number', 'team', 'total-score', 'total-games', 'avg_score']
        extra_kwargs = {
            'first-name': {'source': 'first_name'},
            'last-name': {'source': 'last_name'},
            'player-number': {'source': 'player_number'},
            'total-score': {'source': 'total_score'},
            'total-games': {'source': 'total_games'},
            'avg-score': {'source': 'avg_score'},
        }


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    #teams = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='player-detail')

    class Meta:
        model = Team
        fields = ['id', 'team-name', 'coach', 'players']
        extra_kwargs = {
            'team-name': {'source': 'team_name'},
            'coach': {'source': 'coach_name'},
        }
