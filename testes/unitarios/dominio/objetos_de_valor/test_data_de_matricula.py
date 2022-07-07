from datetime import datetime
from unittest import TestCase

from src.dominio.excecoes import ExcecaoDataDeMatriculaInvalida
from src.dominio.objetos_de_valor import DataDeMatricula


class TestDataDeMatricula(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = '10/10/1990'

        data_de_matricula = DataDeMatricula(valor)

        valor_esperado = datetime.strptime(valor, data_de_matricula.FORMATO)
        self.assertEqual(data_de_matricula.valor, valor_esperado)

    def test_init_QUANDO_dia_contem_um_unico_digito_ENTAO_lanca_excecao_data_de_matricula_invalida(self) -> None:
        valor = '1/10/1990'

        with self.assertRaises(ExcecaoDataDeMatriculaInvalida):
            DataDeMatricula(valor)

    def test_init_QUANDO_valor_contem_letras_ENTAO_lanca_excecao_data_de_matricula_invalida(self) -> None:
        valor = '10/outubro/1990'

        with self.assertRaises(ExcecaoDataDeMatriculaInvalida):
            DataDeMatricula(valor)

    def test_init_QUANDO_ano_contem_somente_dois_digitos_ENTAO_lanca_excecao_data_de_matricula_invalida(self) -> None:
        valor = '10/10/90'

        with self.assertRaises(ExcecaoDataDeMatriculaInvalida):
            DataDeMatricula(valor)

    def test_init_QUANDO_data_nao_existe_ENTAO_lanca_excecao_data_de_matricula_invalida(self) -> None:
        valor = '40/10/1990'

        with self.assertRaises(ExcecaoDataDeMatriculaInvalida):
            DataDeMatricula(valor)

    def test_init_QUANDO_data_esta_no_futuro_ENTAO_lanca_excecao_data_de_matricula_invalida(self) -> None:
        valor = '10/10/2100'

        with self.assertRaises(ExcecaoDataDeMatriculaInvalida):
            DataDeMatricula(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = '10/10/1990'
        data_de_matricula = DataDeMatricula(valor)

        texto = data_de_matricula.texto

        texto_esperado = valor
        self.assertEqual(texto, texto_esperado)
