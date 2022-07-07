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
    def __string(tamanho: int, caracteres: str) -> str:
        return ''.join([random.choice(caracteres) for _ in range(tamanho)])
