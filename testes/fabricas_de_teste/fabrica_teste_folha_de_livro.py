from typing import List

import factory.fuzzy

from src.dominio.glossarios import Glossario
from src.dominio.objetos_de_valor import FolhaDeLivro
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


def construir_opcoes() -> List[str]:
    opcoes = [StringAleatoria.randomizar_caracteres(base=opcao, digito_minimo=1) for opcao in Glossario.exemplos_de_folha_de_livro]
    return [StringAleatoria.garantir_numeros_crescentes(opcao) for opcao in opcoes]


class FabricaTesteFolhaDeLivro(factory.Factory):
    class Meta:
        model = FolhaDeLivro

    valor = factory.fuzzy.FuzzyChoice(construir_opcoes())
