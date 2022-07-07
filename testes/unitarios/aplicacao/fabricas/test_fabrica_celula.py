from unittest import TestCase

from src.aplicacao.fabricas import FabricaCelula
from src.dominio.otds import OTDCelula
from testes.fabricas_de_teste import FabricaTesteCelulaOTD


class TestFabricaCelula(TestCase):
    def setUp(self) -> None:
        self.otd: OTDCelula = FabricaTesteCelulaOTD.build()
        self.fabrica_de_celula = FabricaCelula()

    def test_de_otd_QUANDO_chamado_ENTAO_atribui_conteudo_do_otd_ao_conteudo_da_celula(self) -> None:
        celula = self.fabrica_de_celula.criar_de_otd(self.otd)

        conteudo_esperado = self.otd.conteudo
        self.assertEqual(celula.conteudo, conteudo_esperado)

    def test_de_otd_QUANDO_chamado_ENTAO_atribui_comentario_do_otd_ao_conteudo_da_celula(self) -> None:
        celula = self.fabrica_de_celula.criar_de_otd(self.otd)

        conteudo_esperado = self.otd.comentario
        self.assertEqual(celula.comentario, conteudo_esperado)

    def test_de_otd_QUANDO_chamado_ENTAO_atribui_cor_fundo_do_otd_ao_conteudo_da_celula(self) -> None:
        celula = self.fabrica_de_celula.criar_de_otd(self.otd)

        conteudo_esperado = self.otd.cor_fundo
        self.assertEqual(celula.cor_fundo, conteudo_esperado)

    def test_de_otd_QUANDO_chamado_ENTAO_atribui_cor_text_do_otd_ao_conteudo_da_celula(self) -> None:
        celula = self.fabrica_de_celula.criar_de_otd(self.otd)

        conteudo_esperado = self.otd.cor_texto
        self.assertEqual(celula.cor_texto, conteudo_esperado)
