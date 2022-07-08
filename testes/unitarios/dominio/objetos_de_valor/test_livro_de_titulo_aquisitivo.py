from unittest import TestCase

from src.dominio.excecoes import ExcecaoLivroDeTituloAquisitivoInvalido
from src.dominio.objetos_de_valor.livro_de_titulo_aquisitivo import LivroDeTituloAquisitivo


class TestLivroDeTituloAquisitivo(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        self.assertEqual(livro_de_registro_anterior.valor, valor)

    def test_init_QUANDO_livro_tem_maiusculas_e_minusculas_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'lIvRo 3'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_nao_tem_espaco_entre_livro_e_numero_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro3'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_existe_espacos_no_comeco_e_fim_ENTAO_atribui_valor_esperado(self) -> None:
        valor = ' Livro 3 '

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_letra_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3E'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3E'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_duas_letras_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3AE'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3AE'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_duas_letras_separadas_por_traco_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3A-E'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3AE'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_duas_letras_separadas_por_barra_pra_frente_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3A/E'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3AE'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_duas_letras_separadas_por_barra_pra_tras_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3A\\E'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3AE'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_numeracao_contem_duas_letras_minusculas_ENTAO_atribui_valor_esperado(self) -> None:
        valor = 'Livro 3ae'

        livro_de_registro_anterior = LivroDeTituloAquisitivo(valor)

        valor_esperado = 'Livro 3AE'
        self.assertEqual(livro_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_livro_esta_escrito_errado_ENTAO_lanca_excecao_livro_de_registro_anterior_invalido(self) -> None:
        valor = 'Livo 3'

        with self.assertRaises(ExcecaoLivroDeTituloAquisitivoInvalido):
            LivroDeTituloAquisitivo(valor)

    def test_init_QUANDO_numeracao_nao_tem_numero_ENTAO_lanca_excecao_livro_de_registro_anterior_invalido(self) -> None:
        valor = 'Livro A'

        with self.assertRaises(ExcecaoLivroDeTituloAquisitivoInvalido):
            LivroDeTituloAquisitivo(valor)

    def test_init_QUANDO_numeracao_nao_existe_ENTAO_lanca_excecao_livro_de_registro_anterior_invalido(self) -> None:
        valor = 'Livro'

        with self.assertRaises(ExcecaoLivroDeTituloAquisitivoInvalido):
            LivroDeTituloAquisitivo(valor)
