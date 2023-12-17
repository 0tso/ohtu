from tuomari import Tuomari
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def kaksinpeli():
    pelaa(KPSPelaajaVsPelaaja())

def tekoaly_peli():
    pelaa(KPSTekoaly())

def parannettu_tekoaly_peli():
    pelaa(KPSParempiTekoaly())


def pelaa(siirrot):
    tuomari = Tuomari()

    while True:

        ekan_siirto = siirrot(True)
        tokan_siirto = siirrot(False)
        
        if not (_onko_ok_siirto(ekan_siirto) and _onko_ok_siirto(tokan_siirto)):
            break

        tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    
    print(tuomari)

def _onko_ok_siirto(siirto):
    return siirto == "k" or siirto == "p" or siirto == "s"