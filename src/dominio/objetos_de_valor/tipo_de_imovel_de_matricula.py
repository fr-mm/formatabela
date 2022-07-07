from src.dominio.enums import EnumTipoDeImovel
from src.dominio.excecoes import ExcecaoTipoDeImovelDeMatriculaInvalido
from src.dominio.interfaces import AtributoDeMatricula


class TipoDeImovelDeMatricula(AtributoDeMatricula):
    __valor: EnumTipoDeImovel

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> EnumTipoDeImovel:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor.value

    @staticmethod
    def __validar(valor: str) -> EnumTipoDeImovel:
        try:
            return EnumTipoDeImovel(valor)
        except ValueError:
            raise ExcecaoTipoDeImovelDeMatriculaInvalido(valor)
