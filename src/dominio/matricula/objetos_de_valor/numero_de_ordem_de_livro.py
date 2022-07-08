import re

from src.dominio.matricula.enums import EnumFormatoTituloAquisitivo
from src.dominio.matricula.excecoes import ExcecaoNumeroDeOrdemDeLivro


class NumeroDeOrdemDeLivro:
    __valor: str

    def __init__(self, valor: str) -> None:
        valor_validado = self.__validar(valor)
        valor_formatado = self.__formatar(valor_validado)
        self.__valor = valor_formatado

    @property
    def valor(self) -> str:
        return self.__valor

    def __validar(self, valor: str) -> str:
        valor = valor.strip()
        padrao = EnumFormatoTituloAquisitivo.NUMERO_DE_ORDEM_DE_LIVRO.value
        if not re.match(pattern=padrao, string=valor):
            raise ExcecaoNumeroDeOrdemDeLivro(valor)
        primeiro_digito = valor[self.__extrair_indice_do_primeiro_digito(valor)]
        if primeiro_digito == '0':
            raise ExcecaoNumeroDeOrdemDeLivro(valor)
        return valor

    def __formatar(self, valor: str) -> str:
        indice_do_primeiro_digito = self.__extrair_indice_do_primeiro_digito(valor)
        numero = valor[indice_do_primeiro_digito:]
        if len(numero) > 3 and '.' not in numero:
            comeco = numero[:-3]
            final = numero[-3:]
            numero = f'{comeco}.{final}'
        return f'n° {numero}'

    @staticmethod
    def __extrair_indice_do_primeiro_digito(valor: str) -> int:
        for indice in range(len(valor)):
            caracter = valor[indice]
            if caracter.isdigit():
                return indice
