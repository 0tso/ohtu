class KPSPelaajaVsPelaaja:
    def __init__(self):
        pass

    def __call__(self, vuoro):
        if vuoro:
            return input("Ensimmäisen pelaajan siirto: ")
        else:
            return input("Toisen pelaajan siirto: ")