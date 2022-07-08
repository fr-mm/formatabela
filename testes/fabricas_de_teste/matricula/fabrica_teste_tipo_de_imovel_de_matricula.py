import factory.fuzzy

from src.dominio.matricula.enums import EnumTipoDeImovel
from src.dominio.matricula.objetos_de_valor import TipoDeImovelDeMatricula


class FabricaTesteTipoDeImovelDeMatricula(factory.Factory):
    class Meta:
        model = TipoDeImovelDeMatricula

    valor = factory.fuzzy.FuzzyChoice([tipo_de_imovel.value for tipo_de_imovel in EnumTipoDeImovel])
