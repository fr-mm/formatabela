import random
import string


class Aleatorio:
    @staticmethod
    def texto(tamanho_maximo: int) -> str:
        return Aleatorio.__string(tamanho=random.randrange(tamanho_maximo), caracteres=string.ascii_letters)

    @staticmethod
    def cor_rgb() -> str:
        return Aleatorio.__string(tamanho=8, caracteres='0123456789F')

    @staticmethod
    def data_string_no_passado() -> str:
        dia = Aleatorio.__string_de_numero_com_dois_digitos(maximo=28)
        mes = Aleatorio.__string_de_numero_com_dois_digitos(maximo=12)
        ano = random.randrange(1000, 2021)
        return f'{dia}/{mes}/{ano}'

    @staticmethod
    def __string_de_numero_com_dois_digitos(maximo: int) -> str:
        numero = random.randrange(1, maximo)
        return str(numero).rjust(2, '0')

    @staticmethod
    def __string(tamanho: int, caracteres: str) -> str:
        return ''.join([random.choice(caracteres) for _ in range(tamanho)])
