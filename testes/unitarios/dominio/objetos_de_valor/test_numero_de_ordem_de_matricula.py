from unittest import TestCase

from src.dominio.excecoes import ExcecaoNumeroDeOrdemDeMatriculaInvalido
from src.dominio.objetos_de_valor import NumeroDeOrdemDeMatricula


class TestNumeroDeOrdemDeMatricula(TestCase):
    def test_init_QUANDO_valor_eh_numerico_acima_de_0_ENTAO_retorna_instancia_com_valor_atribuido(self) -> None:
        valor = '1'

        numero_de_ordem_de_matricula = NumeroDeOrdemDeMatricula(valor)

        valor_esperado = 1
        self.assertEqual(numero_de_ordem_de_matricula.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_eh_maior_que_zero_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = '0'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatriculaInvalido):
            NumeroDeOrdemDeMatricula(valor)

    def test_init_QUANDO_valor_nao_eh_numerico_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = 'a'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatriculaInvalido):
            NumeroDeOrdemDeMatricula(valor)

    def test_init_QUANDO_valor_nao_eh_inteiro_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = '1.2'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatriculaInvalido):
            NumeroDeOrdemDeMatricula(valor)
