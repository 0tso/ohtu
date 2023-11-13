from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality, descending=True):
        return sorted(
            filter(lambda player: player.nationality == nationality, self.reader.get_players()),
            key=lambda player: player.points,
            reverse=descending
        )