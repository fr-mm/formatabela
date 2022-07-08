from src.dominio.enums import EnumCoordenadasGeorreferenciadas
from src.dominio.excecoes import ExcecaoCoordenadasGeorreferenciadasInvalida
from src.dominio.interfaces import AtributoDeMatricula


class CoordenadasGeorreferenciadasDeMatricula(AtributoDeMatricula):
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> str:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor

    @staticmethod
    def __validar(valor: str) -> str:
        valor = valor.strip().lower()
        try:
            return EnumCoordenadasGeorreferenciadas(valor).value
        except ValueError:
            raise ExcecaoCoordenadasGeorreferenciadasInvalida(valor)
