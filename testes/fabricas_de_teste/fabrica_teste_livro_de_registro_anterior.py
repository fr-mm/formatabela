import factory.fuzzy

from src.dominio.glossarios import Glossario
from src.dominio.objetos_de_valor.livro_de_registro_anterior import LivroDeRegistroAnterior
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteLivroDeRegistroAnterior(factory.Factory):
    class Meta:
        model = LivroDeRegistroAnterior

    valor = factory.fuzzy.FuzzyChoice([StringAleatoria.randomizar_caracteres(opcao) for opcao in Glossario.exemplos_de_livro_de_registro_anterior])
