import random
from unittest import TestCase

from src.dominio.enums import EnumTipoDeImovel
from src.dominio.excecoes import ExcecaoTipoDeImovelDeMatriculaInvalido
from src.dominio.objetos_de_valor import TipoDeImovelDeMatricula


class TestTipoDeImovelDeMatricula(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_retorna_instancia_com_valor_esperado_atribuido(self) -> None:
        valor = random.choice([tipo_de_imovel.value for tipo_de_imovel in EnumTipoDeImovel])

        tipo_de_imovel_de_matricula = TipoDeImovelDeMatricula(valor)

        valor_esperado = EnumTipoDeImovel(valor)
        self.assertEqual(tipo_de_imovel_de_matricula.valor, valor_esperado)

    def test_init_QUANDO_valor_eh_invalido_ENTAO_lanca_excecao_tipo_de_imovel_invalido(self) -> None:
        valor = 'valor inválido'

        with self.assertRaises(ExcecaoTipoDeImovelDeMatriculaInvalido):
            TipoDeImovelDeMatricula(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = random.choice([tipo_de_imovel.value for tipo_de_imovel in EnumTipoDeImovel])
        tipo_de_imovel_de_matricula = TipoDeImovelDeMatricula(valor)

        texto = tipo_de_imovel_de_matricula.texto

        texto_esperado = valor
        self.assertEqual(texto, texto_esperado)

    def test_eh_igual_a_QUANDO_eh_igual_ENTAO_retorna_true(self) -> None:
        valor = EnumTipoDeImovel.URBANO.value
        tipo_de_imovel_de_matricula1 = TipoDeImovelDeMatricula(valor)
        tipo_de_imovel_de_matricula2 = TipoDeImovelDeMatricula(valor)

        resultdo = tipo_de_imovel_de_matricula1.eh_igual_a(tipo_de_imovel_de_matricula2)

        self.assertTrue(resultdo)

    def test_eh_igual_a_QUANDO_eh_diferente_ENTAO_retorna_false(self) -> None:
        valor1 = EnumTipoDeImovel.URBANO.value
        valor2 = EnumTipoDeImovel.RURAL.value
        tipo_de_imovel_de_matricula1 = TipoDeImovelDeMatricula(valor1)
        tipo_de_imovel_de_matricula2 = TipoDeImovelDeMatricula(valor2)

        resultdo = tipo_de_imovel_de_matricula1.eh_igual_a(tipo_de_imovel_de_matricula2)

        self.assertFalse(resultdo)
