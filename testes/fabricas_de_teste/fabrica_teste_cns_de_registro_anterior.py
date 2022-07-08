import factory.fuzzy

from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.objetos_de_valor import CNSDeRegistroAnterior


class FabricaTesteCNSDeRegistroAnterior(factory.Factory):
    class Meta:
        model = CNSDeRegistroAnterior

    valor = factory.fuzzy.FuzzyChoice([opcao.value for opcao in EnumCNSDeRegistroAnterior])
