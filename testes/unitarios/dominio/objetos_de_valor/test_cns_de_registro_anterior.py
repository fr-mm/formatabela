import random
from unittest import TestCase

from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.excecoes import ExcecaoCNSDeRegistroAnterior
from src.dominio.objetos_de_valor import CNSDeRegistroAnterior


class TestCNSDeRegistroAnterior(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor_esperado(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCNSDeRegistroAnterior])

        cns_de_registro_anterior = CNSDeRegistroAnterior(valor)

        valor_esperado = EnumCNSDeRegistroAnterior(valor)
        self.assertEqual(cns_de_registro_anterior.valor, valor_esperado)

    def test_init_QUANDO_valor_nao_eh_valido_ENTAO_lanca_excecao_cns_de_registro_anterior_invalido(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoCNSDeRegistroAnterior):
            CNSDeRegistroAnterior(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_string_esperada(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCNSDeRegistroAnterior])

        cns_de_registro_anterior = CNSDeRegistroAnterior(valor)

        self.assertEqual(cns_de_registro_anterior.texto, valor)
