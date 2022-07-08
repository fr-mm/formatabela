import factory.fuzzy

from src.dominio.matricula.objetos_de_valor import DataDeMatricula
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteDataDeMatricula(factory.Factory):
    class Meta:
        model = DataDeMatricula

    valor = StringAleatoria.data_no_passado()
