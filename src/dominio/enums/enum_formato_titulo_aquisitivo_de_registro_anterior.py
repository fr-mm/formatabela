from enum import Enum


class EnumFormatoTituloAquisitivoDeRegistroAnterior(Enum):
    NUMERO_DE_ORDEM = r'^(?:\d{1,3})?(?:\.\d{3})|\d{1,6}$'
    LIVRO = r'(?i)livro\ ?\d((:?[\-\.\/\\]?[a-z])?){1,2}'
