import random
import string


class StringAleatoria:
    @staticmethod
    def texto(tamanho_maximo: int) -> str:
        return StringAleatoria.__string(tamanho=random.randrange(tamanho_maximo), caracteres=string.ascii_letters)

    @staticmethod
    def cor_rgb() -> str:
        return StringAleatoria.__string(tamanho=8, caracteres='0123456789F')

    @staticmethod
    def data_no_passado() -> str:
        dia = StringAleatoria.__numero_com_dois_digitos(maximo=28)
        mes = StringAleatoria.__numero_com_dois_digitos(maximo=12)
        ano = random.randrange(1000, 2021)
        return f'{dia}/{mes}/{ano}'

    @staticmethod
    def float(
            minimo: float,
            maximo: float,
    ) -> str:
        numero = random.uniform(minimo, maximo)
        return str(numero)

    @staticmethod
    def substituindo_caracter_por_digito(base: str, substituir: str) -> str:
        resultado = ''
        for caracter in base:
            if caracter == substituir:
                resultado += str(random.randrange(0, 9))
            else:
                resultado += caracter
        return resultado

    @staticmethod
    def __numero_com_dois_digitos(maximo: int) -> str:
        numero = random.randrange(1, maximo)
        return str(numero).rjust(2, '0')

    @staticmethod
    def __string(tamanho: int, caracteres: str) -> str:
        return ''.join([random.choice(caracteres) for _ in range(tamanho)])
