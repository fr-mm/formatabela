from unittest import TestCase

from src.dominio.excecoes import ExcecaoNumeroDeOrdemDeLivro
from src.dominio.objetos_de_valor import NumeroDeOrdemDeLivro


class TestNumeroDeOrdemDeLivro(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'n° 1'

        numero_de_ordem_de_livro = NumeroDeOrdemDeLivro(valor)

        self.assertEqual(numero_de_ordem_de_livro.valor, valor)

    def test_init_QUANDO_nao_tem_bolinha_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'n 1'

        numero_de_ordem_de_livro = NumeroDeOrdemDeLivro(valor)

        valor_esperado = 'n° 1'
        self.assertEqual(numero_de_ordem_de_livro.valor, valor_esperado)

    def test_init_QUANDO_nao_tem_espaco_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'n°1'

        numero_de_ordem_de_livro = NumeroDeOrdemDeLivro(valor)

        valor_esperado = 'n° 1'
        self.assertEqual(numero_de_ordem_de_livro.valor, valor_esperado)

    def test_init_QUANDO_numero_de_quatro_digitos_tem_ponto_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'n° 1.000'

        numero_de_ordem_de_livro = NumeroDeOrdemDeLivro(valor)

        valor_esperado = 'n° 1.000'
        self.assertEqual(numero_de_ordem_de_livro.valor, valor_esperado)

    def test_init_QUANDO_numero_de_quatro_digitos_nao_tem_ponto_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'n° 1000'

        numero_de_ordem_de_livro = NumeroDeOrdemDeLivro(valor)

        valor_esperado = 'n° 1.000'
        self.assertEqual(numero_de_ordem_de_livro.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_eh_valido_ENTAO_lanca_excecao_numero_de_ordem_de_livro_invalido(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeLivro):
            NumeroDeOrdemDeLivro(valor)

    def test_init_QUANDO_numero_comeca_com_zero_ENTAO_lanca_excecao_numero_de_ordem_de_livro_invalido(self) -> None:
        valor = 'n° 010'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeLivro):
            NumeroDeOrdemDeLivro(valor)

