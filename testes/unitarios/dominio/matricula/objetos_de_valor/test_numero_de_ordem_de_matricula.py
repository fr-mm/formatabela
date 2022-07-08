from unittest import TestCase

from src.dominio.matricula.excecoes import ExcecaoNumeroDeOrdemDeMatricula
from src.dominio.matricula.objetos_de_valor import NumeroDeOrdemDeMatricula


class TestNumeroDeOrdemDeMatricula(TestCase):
    def test_init_QUANDO_valor_eh_numerico_acima_de_0_ENTAO_retorna_instancia_com_valor_atribuido(self) -> None:
        valor = '1'

        numero_de_ordem_de_matricula = NumeroDeOrdemDeMatricula(valor)

        valor_esperado = 1
        self.assertEqual(numero_de_ordem_de_matricula.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_eh_maior_que_zero_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = '0'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatricula):
            NumeroDeOrdemDeMatricula(valor)

    def test_init_QUANDO_valor_nao_eh_numerico_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = 'a'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatricula):
            NumeroDeOrdemDeMatricula(valor)

    def test_init_QUANDO_valor_nao_eh_inteiro_ENTAO_lanca_excessao_de_numero_de_ordem_de_matricula(self) -> None:
        valor = '1.2'

        with self.assertRaises(ExcecaoNumeroDeOrdemDeMatricula):
            NumeroDeOrdemDeMatricula(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = '1'
        numero_de_ordem_de_matricula = NumeroDeOrdemDeMatricula(valor)

        texto = numero_de_ordem_de_matricula.texto

        valor_esperado = '1'
        self.assertEqual(texto, valor_esperado)

    def test_eh_igual_a_QUANDO_eh_igual_ENTAO_retorna_true(self) -> None:
        valor = '1'
        numero_de_ordem_de_matricula1 = NumeroDeOrdemDeMatricula(valor)
        numero_de_ordem_de_matricula2 = NumeroDeOrdemDeMatricula(valor)

        resultado = numero_de_ordem_de_matricula1.eh_igual_a(numero_de_ordem_de_matricula2)

        self.assertTrue(resultado)

    def test_eh_igual_a_QUANDO_eh_diferente_ENTAO_retorna_false(self) -> None:
        valor1 = '1'
        valor2 = '2'
        numero_de_ordem_de_matricula1 = NumeroDeOrdemDeMatricula(valor1)
        numero_de_ordem_de_matricula2 = NumeroDeOrdemDeMatricula(valor2)

        resultado = numero_de_ordem_de_matricula1.eh_igual_a(numero_de_ordem_de_matricula2)

        self.assertFalse(resultado)
