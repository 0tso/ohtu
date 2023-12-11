import matchers

class Query:
    def __init__(self) -> None:
        self._matchers = []
        pass

    def playsIn(self, team):
        self._matchers.append(matchers.PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self._matchers.append(matchers.HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(matchers.HasFewerThan(value, attr))
        return self
    
    def oneOf(self, *m):
        self._matchers = [matchers.Or(*m)]
        return self
    
    def test(self, player):
        matcher = matchers.And(*self._matchers)
        return matcher.test(player)