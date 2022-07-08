import re

from src.dominio.enums import EnumFormatoTituloAquisitivo
from src.dominio.excecoes import ExcecaoFolhaDeLivroInvalida


class FolhaDeLivro:
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        self.__valor = valor_validado

    @property
    def valor(self) -> str:
        return self.__valor

    @staticmethod
    def __validar(valor: str) -> str:
        valor = valor.strip()
        padrao = EnumFormatoTituloAquisitivo.FOLHA_DE_LIVRO.value
        if not re.match(pattern=padrao, string=valor):
            raise ExcecaoFolhaDeLivroInvalida(valor)
        numeros = re.findall(r'\d+', valor)
        formatado = f'fl. {numeros[0]}'
        if len(numeros) == 2:
            formatado += f' a {numeros[1]}'
        return formatado
