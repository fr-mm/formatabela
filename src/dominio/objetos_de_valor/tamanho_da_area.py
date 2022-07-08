import re

from src.dominio.excecoes import ExcecaoTamanhoDaArea
from src.dominio.interfaces import AtributoDeMatricula


class TamanhoDaArea(AtributoDeMatricula):
    __valor: float
    __PADRAO_REGEX = r'^\d+[\.\,]?(?:\d+)?$'

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def texto(self) -> str:
        return str(self.valor).replace('.', ',')

    def __validar(self, valor: str) -> float:
        string_valida = self.__validar_caracteres(valor)
        valor_float = self.__validar_float(string_valida)
        positivo = self.__validar_positivo(valor_float)
        return positivo

    def __validar_caracteres(self, valor: str) -> str:
        if not re.match(self.__PADRAO_REGEX, valor):
            raise ExcecaoTamanhoDaArea(valor)
        return valor

    @staticmethod
    def __validar_float(valor: str) -> float:
        valor_sem_espacos = valor.strip()
        valor_com_ponto = valor_sem_espacos.replace(',', '.')
        try:
            valor_float = float(valor_com_ponto)
            return round(valor_float, 4)
        except ValueError:
            raise ExcecaoTamanhoDaArea(valor)

    @staticmethod
    def __validar_positivo(valor: float) -> float:
        if valor < 0:
            raise ExcecaoTamanhoDaArea(str(valor))
        return valor
