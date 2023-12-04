OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = OLETUSKAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self._lista = self._luo_lista(self.kapasiteetti)

        self._käytetty = 0

    def kuuluu(self, n):
        return n in self._lista

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self._lista[self._käytetty] = n
        self._käytetty = self._käytetty + 1

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self._käytetty == len(self._lista):
            taulukko_old = self._lista
            self._lista = self._luo_lista(self._käytetty + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self._lista)
        return True

    def poista(self, n):
        kohta = -1
        try:
            kohta = self._lista.index(n)
        except ValueError:
            return False
        
        self.kopioi_lista(self._lista, self._lista, a_alku=kohta+1, b_alku=kohta)
        self._lista[self._käytetty] = 0
        self._käytetty -= 1
        return True

    def mahtavuus(self):
        return self._käytetty

    def to_int_list(self):
        taulu = self._luo_lista(self._käytetty)
        self.kopioi_lista(self._lista, taulu, a_loppu=self._käytetty)
        return taulu

    @staticmethod
    def kopioi_lista(a, b, a_alku=0, b_alku=0, a_loppu=None):
        määrä = (a_loppu or len(a)) - a_alku
        for i in range(0, määrä):
            b[b_alku + i] = a[a_alku + i]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for n in a.to_int_list() + b.to_int_list():
            x.lisaa(n)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self._käytetty == 0:
            return "{}"
        elif self._käytetty == 1:
            return "{" + str(self._lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self._käytetty - 1):
                tuotos = tuotos + str(self._lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self._lista[self._käytetty - 1])
            tuotos = tuotos + "}"
            return tuotos
