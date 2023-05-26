from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=20)
    coach_name = models.CharField(max_length=60)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_number = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    height = models.FloatField()
    total_score = models.IntegerField()
    total_games = models.IntegerField()
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([str(self.first_name), str(self.last_name)])

    # @property
    # def avg_score(self):
    #     return float(self.total_score)/float(self.total_games)



