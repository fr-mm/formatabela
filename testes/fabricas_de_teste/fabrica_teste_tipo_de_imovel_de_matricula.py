import factory.fuzzy

from src.dominio.enums import EnumTipoDeImovel
from src.dominio.objetos_de_valor import TipoDeImovelDeMatricula


class FabricaTesteTipoDeImovelDeMatricula(factory.Factory):
    class Meta:
        model = TipoDeImovelDeMatricula

    valor = factory.fuzzy.FuzzyChoice([tipo_de_imovel.value for tipo_de_imovel in EnumTipoDeImovel])
