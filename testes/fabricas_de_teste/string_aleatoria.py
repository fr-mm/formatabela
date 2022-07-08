import random
import re
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
    def randomizar_caracteres(base: str, digito_minimo: int = 0) -> str:
        """
        Retorna string base substituindo:
        0 por dígito
        A por letra maiúsculas
        """
        resultado = ''
        for caracter in base:
            if caracter == '0':
                resultado += str(random.randrange(digito_minimo, 9))
            elif caracter == 'A':
                resultado += random.choice(string.ascii_uppercase)
            else:
                resultado += caracter
        return resultado

    @staticmethod
    def garantir_numeros_crescentes(texto: str) -> str:
        numeros = re.findall(r'\d+', texto)
        if len(numeros) < 2:
            return texto
        numeros_ordenados = numeros.copy()
        numeros_ordenados.sort()
        for indice in range(len(numeros)):
            texto.replace(numeros[indice], numeros_ordenados[indice])
        return texto

    @staticmethod
    def __numero_com_dois_digitos(maximo: int) -> str:
        numero = random.randrange(1, maximo)
        return str(numero).rjust(2, '0')

    @staticmethod
    def __string(tamanho: int, caracteres: str) -> str:
        return ''.join([random.choice(caracteres) for _ in range(tamanho)])
