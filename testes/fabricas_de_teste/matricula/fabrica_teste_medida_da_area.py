import factory.fuzzy

from src.dominio.matricula.enums import EnumMedidaDaArea
from src.dominio.matricula.objetos_de_valor import MedidaDaArea


class FabricaTesteMedidaDaArea(factory.Factory):
    class Meta:
        model = MedidaDaArea

    valor = factory.fuzzy.FuzzyChoice([medida_da_area.value for medida_da_area in EnumMedidaDaArea])
