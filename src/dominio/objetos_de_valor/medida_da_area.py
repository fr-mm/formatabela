from src.dominio.enums import EnumMedidaDaArea
from src.dominio.excecoes import ExcecaoMedidaDaAreaInvalida
from src.dominio.interfaces import AtributoDeMatricula


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
            raise ExcecaoMedidaDaAreaInvalida(valor)
