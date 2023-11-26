import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viite_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)
        self.viite_mock.uusi.return_value = 123

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self.viite_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirto_oikeilla_argumenteilla(self):
        self.viite_mock.uusi.return_value = 70
        self.varasto_mock.saldo.return_value = 3
        self.varasto_mock.hae_tuote.return_value = Tuote(7, "mehu", 2)

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(7)
        kauppa.tilimaksu("Heikki Heikkinen", "12346")

        self.pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 70, "12346", ANY, 2)

    def test_tilisiirto_usealla_tuotteella(self):
        self.viite_mock.uusi.return_value = 35
        self.varasto_mock.saldo.return_value = 2
        self.varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "a", 4) if x == 1 else Tuote(2, "b", 9)

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Heikki Heikkinen", "12346")

        self.pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 35, "12346", ANY, 13)
    
    def test_tilisiirto_usealla_samalla_tuotteella(self):
        self.viite_mock.uusi.return_value = 89
        self.varasto_mock.saldo.return_value = 2
        self.varasto_mock.hae_tuote.return_value = Tuote(1, "a", 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Heikki Heikkinen", "12346")

        self.pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 89, "12346", ANY, 10)
    
    def test_tilisiirto_loppuunmyydylla_tuotteella(self):
        self.varasto_mock.saldo.side_effect = lambda x: 0 if x == 1 else 1
        self.varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "ac", 5) if x == 1 else Tuote(2, "oiacwm", 123)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Heikki Heikkinen", "12346")

        self.pankki_mock.tilisiirto.assert_called_with("Heikki Heikkinen", 123, "12346", ANY, 123)

    def test_uusi_alku_nollaa_aiemman_ostoksen(self):
        self.varasto_mock.saldo.return_value = 2
        self.varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "ac", 5) if x == 1 else Tuote(2, "oiacwm", 10)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Matti Mattinen", "12346")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Mattinen", 123, "12346", ANY, 10)

        self.viite_mock.uusi.return_value = 612

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("Jukka Jukkanen", "6123")
        self.pankki_mock.tilisiirto.assert_called_with("Jukka Jukkanen", 612, "6123", ANY, 5)
    
    def test_poista_tuote(self):
        self.varasto_mock.saldo.return_value = 2
        self.varasto_mock.hae_tuote.side_effect = lambda x: Tuote(1, "ac", 5) if x == 1 else Tuote(2, "oiacwm", 10)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("Matti Mattinen", "12346")
        self.pankki_mock.tilisiirto.assert_called_with("Matti Mattinen", 123, "12346", ANY, 5)