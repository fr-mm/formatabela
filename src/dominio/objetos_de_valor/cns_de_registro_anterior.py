from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.excecoes import ExcecaoCNSDeRegistroAnterior
from src.dominio.interfaces import AtributoDeMatricula


class CNSDeRegistroAnterior(AtributoDeMatricula):
    __valor: EnumCNSDeRegistroAnterior

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> EnumCNSDeRegistroAnterior:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor.value

    @staticmethod
    def __validar(valor) -> EnumCNSDeRegistroAnterior:
        try:
            return EnumCNSDeRegistroAnterior(valor)
        except ValueError:
            raise ExcecaoCNSDeRegistroAnterior(valor)
