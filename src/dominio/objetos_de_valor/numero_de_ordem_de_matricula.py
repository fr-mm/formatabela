from src.dominio.excecoes import ExcecaoNumeroDeOrdemDeMatricula
from src.dominio.interfaces import AtributoDeMatricula


class NumeroDeOrdemDeMatricula(AtributoDeMatricula):
    __valor: int

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> int:
        return self.__valor

    @property
    def texto(self) -> str:
        return str(self.valor)

    def __validar(self, valor: str) -> int:
        valor_inteiro = self.__validar_inteiro(valor)
        return self.__validar_maior_que_zero(valor_inteiro)

    @staticmethod
    def __validar_inteiro(valor: str) -> int:
        try:
            return int(valor)
        except ValueError:
            raise ExcecaoNumeroDeOrdemDeMatricula(valor)

    @staticmethod
    def __validar_maior_que_zero(valor_inteiro: int) -> int:
        if not valor_inteiro > 0:
            raise ExcecaoNumeroDeOrdemDeMatricula(str(valor_inteiro))
        return valor_inteiro
