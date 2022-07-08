from enum import Enum


class EnumFormatoTituloAquisitivo(Enum):
    NUMERO_DE_ORDEM_DE_LIVRO = r'(?i)^n°? ?((?:\d{1,3})?(?:\.\d{3})|\d{1,6})$'
    LIVRO = r'(?i)livro\ ?\d((:?[\-\.\/\\]?[a-z])?){1,2}'
