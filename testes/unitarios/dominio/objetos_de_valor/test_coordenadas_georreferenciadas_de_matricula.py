import random
from unittest import TestCase

from src.dominio.enums import EnumCoordenadasGeorreferenciadas
from src.dominio.excecoes import ExcecaoCoordenadasGeorreferenciadasInvalida
from src.dominio.objetos_de_valor import CoordenadasGeorreferenciadasDeMatricula


class TestCoordenadasGeorreferenciadasDeMatricula(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor_esperado(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCoordenadasGeorreferenciadas])

        coordenadas_georreferenciadas = CoordenadasGeorreferenciadasDeMatricula(valor)

        valor_esperado = EnumCoordenadasGeorreferenciadas(valor)
        self.assertEqual(coordenadas_georreferenciadas.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_eh_valido_ENTAO_lanca_excecao_coordenadas_georreferenciadas_invalida(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoCoordenadasGeorreferenciadasInvalida):
            CoordenadasGeorreferenciadasDeMatricula(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCoordenadasGeorreferenciadas])

        coordenadas_georreferenciadas = CoordenadasGeorreferenciadasDeMatricula(valor)

        self.assertEqual(coordenadas_georreferenciadas.texto, valor)
