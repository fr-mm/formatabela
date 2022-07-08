import re

from src.dominio.enums import EnumFormatoInscricaoImobiliariaMunicipalDeMatricula
from src.dominio.excecoes import ExcecaoInscricaoImobiliariaMunicipalInvalida
from src.dominio.interfaces import AtributoDeMatricula


class InscricaoImobiliariaMunicipalDeMatricula(AtributoDeMatricula):
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
        formatos = [formato.value for formato in EnumFormatoInscricaoImobiliariaMunicipalDeMatricula]
        for formato in formatos:
            if re.match(formato, valor):
                return valor
        raise ExcecaoInscricaoImobiliariaMunicipalInvalida(valor)

