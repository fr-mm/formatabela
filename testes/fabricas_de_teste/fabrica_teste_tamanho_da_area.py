import factory.fuzzy

from src.dominio.objetos_de_valor import TamanhoDaArea
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteTamanhoDaArea(factory.Factory):
    class Meta:
        model = TamanhoDaArea

    valor = factory.fuzzy.FuzzyChoice(['0', StringAleatoria.float(0, 20000000000)])
