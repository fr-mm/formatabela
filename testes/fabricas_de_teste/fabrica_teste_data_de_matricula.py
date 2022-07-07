import factory.fuzzy

from src.dominio.objetos_de_valor import DataDeMatricula
from testes.fabricas_de_teste.aleatorio import Aleatorio


class FabricaTesteDataDeMatricula(factory.Factory):
    class Meta:
        model = DataDeMatricula

    valor = Aleatorio.data_string_no_passado()

print(FabricaTesteDataDeMatricula.build().valor)
