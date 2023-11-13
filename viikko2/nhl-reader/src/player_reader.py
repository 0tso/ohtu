import requests
from player import Player

class PlayerReader:
    def __init__(self, url) -> None:
        response = requests.get(url).json()
        self.players = [Player(player_data) for player_data in response]
    
    def get_players(self) -> list[Player]:
        return self.players