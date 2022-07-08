import random
from unittest import TestCase

from src.dominio.enums import EnumMedidaDaArea
from src.dominio.excecoes import ExcecaoMedidaDaAreaInvalida
from src.dominio.objetos_de_valor import MedidaDaArea


class TestMedidaDaArea(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_retorna_instancia_com_valor_esperado(self) -> None:
        valor = random.choice([medida_da_area.value for medida_da_area in EnumMedidaDaArea])

        medida_da_area = MedidaDaArea(valor)

        valor_esperado = EnumMedidaDaArea(valor)
        self.assertEqual(medida_da_area.valor, valor_esperado)

    def test_init_QUANDO_valor_eh_invalido_ENTAO_lanca_excecao_medida_da_area_invalida(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoMedidaDaAreaInvalida):
            MedidaDaArea(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_texto_esperado(self) -> None:
        valor = random.choice([medida_da_area.value for medida_da_area in EnumMedidaDaArea])
        medida_da_area = MedidaDaArea(valor)

        texto = medida_da_area.texto

        self.assertEqual(texto, valor)
