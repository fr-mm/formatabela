import factory.fuzzy

from src.dominio.matricula.glossarios import Glossario
from src.dominio.matricula.objetos_de_valor.livro_de_titulo_aquisitivo import LivroDeTituloAquisitivo
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteLivroDeTituloAquisitivo(factory.Factory):
    class Meta:
        model = LivroDeTituloAquisitivo

    valor = factory.fuzzy.FuzzyChoice([StringAleatoria.randomizar_caracteres(opcao) for opcao in Glossario.exemplos_de_livro_de_registro_anterior])
