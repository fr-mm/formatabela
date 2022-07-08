import random
from unittest import TestCase

from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.excecoes import ExcecaoCNSDeRegistroAnteriorInvalido
from src.dominio.objetos_de_valor import CNSDeRegistroAnterior


class TestCNSDeRegistroAnterior(TestCase):
    def test_init_QUANDO_valor_eh_valido_ENTAO_atribui_valor(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCNSDeRegistroAnterior])

        cns_de_registro_anterior = CNSDeRegistroAnterior(valor)

        self.assertEqual(cns_de_registro_anterior.valor, valor)

    def test_init_QUANDO_valor_nao_eh_valido_ENTAO_lanca_excecao_cns_de_registro_anterior_invalido(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoCNSDeRegistroAnteriorInvalido):
            CNSDeRegistroAnterior(valor)

    def test_texto_QUANDO_chamado_ENTAO_retorna_string_esperada(self) -> None:
        valor = random.choice([opcao.value for opcao in EnumCNSDeRegistroAnterior])

        cns_de_registro_anterior = CNSDeRegistroAnterior(valor)

        self.assertEqual(cns_de_registro_anterior.texto, valor)