from src.dominio.enums import EnumCNSDeRegistroAnterior
from src.dominio.excecoes import ExcecaoCNSDeRegistroAnteriorInvalido
from src.dominio.interfaces import AtributoDeMatricula


class CNSDeRegistroAnterior(AtributoDeMatricula):
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self):
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor

    @staticmethod
    def __validar(valor) -> str:
        try:
            return EnumCNSDeRegistroAnterior(valor).value
        except ValueError:
            raise ExcecaoCNSDeRegistroAnteriorInvalido(valor)
