import factory

from src.dominio.matricula.agregados import AreaDeMatricula
from testes.fabricas_de_teste.matricula.fabrica_teste_medida_da_area import FabricaTesteMedidaDaArea
from testes.fabricas_de_teste.matricula.fabrica_teste_tamanho_da_area import FabricaTesteTamanhoDaArea


class FabricaTesteAreaDeMatricula(factory.Factory):
    class Meta:
        model = AreaDeMatricula

    tamanho = factory.SubFactory(FabricaTesteTamanhoDaArea)
    medida = factory.SubFactory(FabricaTesteMedidaDaArea)
