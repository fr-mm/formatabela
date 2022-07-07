import random
import string

import factory.fuzzy

from src.dominio.otds import OTDCelula


def gerar_string_aleatoria(tamanho: int, caracteres: str) -> str:
    return ''.join([random.choice(caracteres) for _ in range(tamanho)])


def gerar_texto_aleatorio() -> str:
    return gerar_string_aleatoria(tamanho=random.randrange(40), caracteres=string.ascii_letters)


def gerar_cor_rgb_aleatoria() -> str:
    return gerar_string_aleatoria(tamanho=8, caracteres='0123456789F')


class FabricaTesteCelulaOTD(factory.Factory):
    class Meta:
        model = OTDCelula

    conteudo = factory.fuzzy.FuzzyChoice(['', gerar_texto_aleatorio()])
    comentario = factory.fuzzy.FuzzyChoice(['', gerar_texto_aleatorio()])
    cor_fundo = factory.fuzzy.FuzzyChoice(['', gerar_cor_rgb_aleatoria()])
    cor_texto = factory.fuzzy.FuzzyChoice(['', gerar_cor_rgb_aleatoria()])
