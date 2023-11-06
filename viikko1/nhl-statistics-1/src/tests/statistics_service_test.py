import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 1, 1),
            Player("Lemieux", "PIT", 0, 8),
            Player("Kurri",   "EDM", 7, 0),
            Player("Yzerman", "DET", 6, 6),
            Player("Gretzky", "EDM", 0, 0)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_fetch(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.goals, 7)

        player = self.stats.search("Luukkainen")
        self.assertEqual(player, None)
    
    def test_team_fetch(self):
        players = self.stats.team("PIT")
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Lemieux")

    def test_top(self):
        players = self.stats.top(2)
        self.assertEqual(players[0].name, "Yzerman")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(len(players), 2)

        players = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(players[0].name, "Kurri")

        players = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Lemieux")