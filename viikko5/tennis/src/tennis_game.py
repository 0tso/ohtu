ADVANTAGE_THRESHOLD = 4
ADVANTAGE_TITLES = ["Advantage ", "Win for "]
TIE_TITLES = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
SCORE_TITLES = ["Love", "Fifteen", "Thirty", "Forty"]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
    
    def _advantage(self, diff):
        player_name = self.player1_name if diff > 0 else self.player2_name
        abs_diff = abs(diff) - 1
        return ADVANTAGE_TITLES[min(abs_diff, 1)] + player_name
    
    def _format_score(self, score1, score2):
        return f"{score1}-{score2}"

    def get_score(self):
        diff = self.m_score1 - self.m_score2

        if diff == 0:
            return TIE_TITLES[min(self.m_score1, 3)]

        if self.m_score1 >= ADVANTAGE_THRESHOLD or self.m_score2 >= ADVANTAGE_THRESHOLD:
            return self._advantage(diff)
        
        return self._format_score(SCORE_TITLES[self.m_score1], SCORE_TITLES[self.m_score2])