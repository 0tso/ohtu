from tekoaly import Tekoaly

class KPSTekoaly:
    def __init__(self):
        self._tekoäly = Tekoaly()

    def __call__(self, vuoro):
        if vuoro:
            return input("Ensimmäisen pelaajan siirto: ")
        else:
            a = self._tekoäly.anna_siirto()
            print(f"Tekoäly valitsi: {a}")
            return a