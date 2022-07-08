import re
from datetime import datetime, date

from src.dominio.enums import EnumFormatoDataDeMatricula
from src.dominio.excecoes import ExcecaoDataDeMatricula
from src.dominio.interfaces import AtributoDeMatricula


class DataDeMatricula(AtributoDeMatricula):
    __valor: date

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> date:
        return self.__valor

    @property
    def texto(self) -> str:
        return self.valor.strftime(EnumFormatoDataDeMatricula.DATETIME.value)

    def __validar(self, valor: str) -> date:
        valor_com_formato_valido = self.__validar_formato(valor)
        valor_datetime = self.__validar_existencia(valor_com_formato_valido)
        valor_no_passado = self.__validar_no_passado(valor_datetime)
        return valor_no_passado

    @staticmethod
    def __validar_formato(valor: str) -> str:
        if not re.match(
                pattern=EnumFormatoDataDeMatricula.REGEX.value,
                string=valor
        ):
            raise ExcecaoDataDeMatricula(valor)
        return valor

    @staticmethod
    def __validar_existencia(valor: str) -> datetime:
        try:
            return datetime.strptime(
                valor,
                EnumFormatoDataDeMatricula.DATETIME.value
            )
        except ValueError:
            raise ExcecaoDataDeMatricula(valor)

    @staticmethod
    def __validar_no_passado(valor: datetime) -> date:
        if not valor < datetime.now():
            raise ExcecaoDataDeMatricula(valor.strftime(EnumFormatoDataDeMatricula.DATETIME.value))
        return valor.date()
