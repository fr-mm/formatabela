import factory.fuzzy

from src.dominio.matricula.objetos_de_valor import NumeroDeOrdemDeMatricula


class FabricaTesteNumeroDeOrdemDeMatricula(factory.Factory):
    class Meta:
        model = NumeroDeOrdemDeMatricula

    valor = factory.fuzzy.FuzzyInteger(low=1, high=100000)
