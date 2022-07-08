import factory.fuzzy

from src.dominio.matricula.enums import EnumCNSDeRegistroAnterior
from src.dominio.matricula.objetos_de_valor import CNSDeRegistroAnterior


class FabricaTesteCNSDeRegistroAnterior(factory.Factory):
    class Meta:
        model = CNSDeRegistroAnterior

    valor = factory.fuzzy.FuzzyChoice([opcao.value for opcao in EnumCNSDeRegistroAnterior])
