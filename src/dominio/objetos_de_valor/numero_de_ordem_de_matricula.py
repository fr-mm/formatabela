from src.dominio.excecoes import ExcecaoNumeroDeOrdemDeMatriculaInvalido
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

    @staticmethod
    def __validar(valor: str) -> int:
        try:
            valor_inteiro = int(valor)
            if not valor_inteiro > 0:
                raise ExcecaoNumeroDeOrdemDeMatriculaInvalido(valor)
            return valor_inteiro
        except ValueError:
            raise ExcecaoNumeroDeOrdemDeMatriculaInvalido(valor)