from src.dominio.matricula.enums import EnumMedidaDaArea
from src.dominio.matricula.excecoes import ExcecaoMedidaDaArea
from src.dominio.matricula.interfaces import AtributoDeMatricula


class MedidaDaArea(AtributoDeMatricula):
    __valor: EnumMedidaDaArea

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> EnumMedidaDaArea:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor.value

    @staticmethod
    def __validar(valor: str) -> EnumMedidaDaArea:
        try:
            return EnumMedidaDaArea(valor)
        except ValueError:
            raise ExcecaoMedidaDaArea(valor)
