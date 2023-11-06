from player_reader import PlayerReader

from enum import Enum

class SortBy(Enum):
    POINTS = lambda x: x.points
    GOALS = lambda x: x.goals
    ASSISTS = lambda x: x.assists

class StatisticsService:
    def __init__(self, reader):
        reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, method=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=method
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
