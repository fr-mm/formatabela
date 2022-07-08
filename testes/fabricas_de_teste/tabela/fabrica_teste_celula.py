import factory.fuzzy

from src.dominio.tabela.entidades import Celula
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteCelula(factory.Factory):
    class Meta:
        model = Celula

    conteudo = factory.fuzzy.FuzzyChoice(['', StringAleatoria.texto(tamanho_maximo=20)])
    comentario = factory.fuzzy.FuzzyChoice(['', StringAleatoria.texto(tamanho_maximo=40)])
    cor_fundo = factory.fuzzy.FuzzyChoice(['', StringAleatoria.cor_rgb()])
    cor_texto = factory.fuzzy.FuzzyChoice(['', StringAleatoria.cor_rgb()])

