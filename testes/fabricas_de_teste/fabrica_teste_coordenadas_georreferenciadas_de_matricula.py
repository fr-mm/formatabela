import factory.fuzzy

from src.dominio.enums import EnumCoordenadasGeorreferenciadas
from src.dominio.objetos_de_valor import CoordenadasGeorreferenciadasDeMatricula


class FabricaTesteCoordenadasGeorreferenciadasDeMatricula(factory.Factory):
    class Meta:
        model = CoordenadasGeorreferenciadasDeMatricula

    valor = factory.fuzzy.FuzzyChoice([opcao.value for opcao in EnumCoordenadasGeorreferenciadas])
