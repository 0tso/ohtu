from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly:
    def __init__(self):
        self._tekoäly = TekoalyParannettu(10)

    def __call__(self, vuoro):
        if vuoro:
            a = input("Ensimmäisen pelaajan siirto: ")
            self._tekoäly.aseta_siirto(a)
            return a
        else:
            a = self._tekoäly.anna_siirto()
            print(f"Tekoäly valitsi: {a}")
            return a