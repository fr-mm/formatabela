import re
from datetime import datetime

from src.dominio.excecoes import ExcecaoDataDeMatriculaInvalida
from src.dominio.interfaces import AtributoDeMatricula


class DataDeMatricula(AtributoDeMatricula):
    __valor: datetime
    __FORMATO_REGEX = r'([0-9]{2})\/([0-9]{2})\/([0-9]{4})'
    __FORMATO_DATETIME = '%d/%M/%Y'

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> datetime:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor.strftime(self.__FORMATO_DATETIME)

    @property
    def FORMATO(self) -> str:
        return self.__FORMATO_DATETIME

    def __validar(self, valor: str) -> datetime:
        valor_com_formato_valido = self.__validar_formato(valor)
        valor_datetime = self.__validar_existencia(valor_com_formato_valido)
        valor_no_passado = self.__validar_no_passado(valor_datetime)
        return valor_no_passado

    def __validar_formato(self, valor: str) -> str:
        if not re.match(pattern=self.__FORMATO_REGEX, string=valor):
            raise ExcecaoDataDeMatriculaInvalida(valor)
        return valor

    def __validar_existencia(self, valor: str) -> datetime:
        try:
            return datetime.strptime(valor, self.__FORMATO_DATETIME)
        except ValueError:
            raise ExcecaoDataDeMatriculaInvalida(valor)

    def __validar_no_passado(self, valor: datetime) -> datetime:
        if not valor < datetime.now():
            raise ExcecaoDataDeMatriculaInvalida(valor.strftime(self.__FORMATO_DATETIME))
        return valor
