from enum import Enum


class EnumFormatoDataDeMatricula(Enum):
    REGEX = r'(\d{2})\/(\d{2})\/(\d{4})'
    DATETIME = '%d/%m/%Y'
