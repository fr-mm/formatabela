from unittest import TestCase

from src.dominio.excecoes import ExcecaoFolhaDeLivro
from src.dominio.objetos_de_valor import FolhaDeLivro


class TestFolhaDeLivro(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'fl. 3'

        folha_de_livro = FolhaDeLivro(valor)

        self.assertEqual(folha_de_livro.valor, valor)

    def test_init_QUANDO_possui_dois_numeros_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'fl. 12 a 34'

        folha_de_livro = FolhaDeLivro(valor)

        self.assertEqual(folha_de_livro.valor, valor)

    def test_init_QUANDO_falta_ponto_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'fl 1'

        folha_de_livro = FolhaDeLivro(valor)

        valor_esperado = 'fl. 1'
        self.assertEqual(folha_de_livro.valor, valor_esperado)

    def test_init_QUANDO_faltam_espacos_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'fl.1a2'

        folha_de_livro = FolhaDeLivro(valor)

        valor_esperado = 'fl. 1 a 2'
        self.assertEqual(folha_de_livro.valor, valor_esperado)

    def test_init_QUANDO_fl_escrito_errado_ENTAO_lanca_excecao_folha_de_livro_invalda(self) -> None:
        valor = 'fi. 1'

        with self.assertRaises(ExcecaoFolhaDeLivro):
            FolhaDeLivro(valor)

    def test_init_QUANDO_falta_letra_entr_numeros_nao_eh_e_nem_a_ENTAO_lanca_excecao_folha_de_livro_invalda(self) -> None:
        valor = 'fi. 1 o 2'

        with self.assertRaises(ExcecaoFolhaDeLivro):
            FolhaDeLivro(valor)
