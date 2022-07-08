from unittest import TestCase

from src.dominio.matricula.excecoes import ExcecaoInscricaoImobiliariaMunicipal
from src.dominio.matricula.objetos_de_valor import InscricaoImobiliariaMunicipalDeMatricula


class TestInscricaoImobiliariaMunicipalDeMatricula(TestCase):
    def test_init_QUANTO_valor_sao_seis_digitos_sem_ponto_ENTAO_atribui_valor(self) -> None:
        valor = '123456'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_sao_seis_digitos_com_ponto_ENTAO_atribui_valor(self) -> None:
        valor = '123.456'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_sao_seis_digitos_com_traco_na_quarta_ENTAO_atribui_valor(self) -> None:
        valor = '123-456'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_sao_seis_digitos_com_traco_na_quinta_ENTAO_atribui_valor(self) -> None:
        valor = '1234-56'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_sao_quinze_digitos_sem_ponto_ENTAO_atribui_valor(self) -> None:
        valor = '123456789098765'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_sao_quinze_digitos_com_pontos_ENTAO_atribui_valor(self) -> None:
        valor = '12.34.567.89098.765'

        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        self.assertEqual(incricao_imobiliaria_municipal.valor, valor)

    def test_init_QUANTO_valor_eh_invalido_ENTAO_lanca_excecao_inscricao_imobiliaria_municipal_invalida(self) -> None:
        valor = 'valor invalido'

        with self.assertRaises(ExcecaoInscricaoImobiliariaMunicipal):
            InscricaoImobiliariaMunicipalDeMatricula(valor)

    def test_texto_QUANTO_chamada_ENTAO_retorna_texto_esperado(self) -> None:
        valor = '123.456'
        incricao_imobiliaria_municipal = InscricaoImobiliariaMunicipalDeMatricula(valor)

        texto = incricao_imobiliaria_municipal.texto

        self.assertEqual(texto, valor)
