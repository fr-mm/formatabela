from unittest import TestCase

from src.dominio.excecoes import ExcecaoTamanhoDaArea
from src.dominio.objetos_de_valor import TamanhoDaArea


class TestTamanhoDaArea(TestCase):
    def test_init_QUANDO_valor_tem_ponto_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = '1.2345'

        tamanho_da_area = TamanhoDaArea(valor)

        valor_esperado = 1.2345
        self.assertEqual(tamanho_da_area.valor, valor_esperado)

    def test_init_QUANDO_valor_tem_virgula_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = '1,2345'

        tamanho_da_area = TamanhoDaArea(valor)

        valor_esperado = 1.2345
        self.assertEqual(tamanho_da_area.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_tem_casas_decimais_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = '1'

        tamanho_da_area = TamanhoDaArea(valor)

        valor_esperado = 1
        self.assertEqual(tamanho_da_area.valor, valor_esperado)

    def test_init_QUANDO_valor_tem_mais_de_5_casas_decimais_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = '1.23456'

        tamanho_da_area = TamanhoDaArea(valor)

        valor_esperado = 1.2346
        self.assertEqual(tamanho_da_area.valor, valor_esperado)

    def test_init_QUANDO_valor_contem_letra_ENTAO_lanca_excessao_tamanho_de_area_invalido(self) -> None:
        valor = '1e23'

        with self.assertRaises(ExcecaoTamanhoDaArea):
            TamanhoDaArea(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = '1,2345'
        tamanho_da_area = TamanhoDaArea(valor)

        texto = tamanho_da_area.texto

        texto_eserado = '1,2345'
        self.assertEqual(texto, texto_eserado)
