import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirto_oikeilla_argumenteilla(self):
        pankki_mock = Mock()
        Viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        Viitegeneraattori_mock.uusi.return_value = 70
        varasto_mock.saldo.return_value = 3
        varasto_mock.hae_tuote.return_value = Tuote(7, "mehu", 2)

        kauppa = Kauppa(varasto_mock, pankki_mock, Viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(7)
        kauppa.tilimaksu("Heikki Heikkinen", "12346")

        pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 70, "12346", ANY, 2)

    def test_tilisiirto_usealla_tuotteella(self):
        pankki_mock = Mock()
        Viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        Viitegeneraattori_mock.uusi.return_value = 35
        varasto_mock.saldo.return_value = 2
        varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "a", 4) if x == 1 else Tuote(2, "b", 9)

        kauppa = Kauppa(varasto_mock, pankki_mock, Viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Heikki Heikkinen", "12346")

        pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 35, "12346", ANY, 13)