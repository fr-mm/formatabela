import re
from typing import List

from src.dominio.enums import EnumFormatoTituloAquisitivo
from src.dominio.excecoes import ExcecaoLivroDeTituloAquisitivo


class LivroDeTituloAquisitivo:
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        valor_formatado = self.__formatar_valor_validado(valor_validado)
        self.__valor = valor_formatado

    @property
    def valor(self) -> str:
        return self.__valor

    @staticmethod
    def __validar(valor: str) -> str:
        valor = valor.strip()
        padrao = EnumFormatoTituloAquisitivo.LIVRO.value
        if not re.match(pattern=padrao, string=valor):
            raise ExcecaoLivroDeTituloAquisitivo(valor)
        return valor

    def __formatar_valor_validado(self, valor: str) -> str:
        numeracao = valor[5:].strip().upper()
        numeracao = self.__remover_caracteres(texto=numeracao, caracteres=['-', '/', '\\'])
        return f'Livro {numeracao}'

    @staticmethod
    def __remover_caracteres(texto: str, caracteres: List[str]) -> str:
        for caracter in caracteres:
            texto = texto.replace(caracter, '')
        return texto
