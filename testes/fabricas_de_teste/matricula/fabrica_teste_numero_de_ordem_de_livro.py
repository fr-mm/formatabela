import factory.fuzzy

from src.dominio.matricula.glossarios import Glossario
from src.dominio.matricula.objetos_de_valor import NumeroDeOrdemDeLivro
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteNumeroDeOrdemDeLivro(factory.Factory):
    class Meta:
        model = NumeroDeOrdemDeLivro

    valor = factory.fuzzy.FuzzyChoice([StringAleatoria.randomizar_caracteres(opcao, digito_minimo=1) for opcao in Glossario.exemplos_de_numero_de_ordem_de_livro])
