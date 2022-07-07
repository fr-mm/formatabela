import factory.fuzzy

from src.dominio.entidades import Celula
from testes.fabricas_de_teste.aleatorio import Aleatorio


class FabricaTesteCelula(factory.Factory):
    class Meta:
        model = Celula

    conteudo = factory.fuzzy.FuzzyChoice(['', Aleatorio.texto(tamanho_maximo=20)])
    comentario = factory.fuzzy.FuzzyChoice(['', Aleatorio.texto(tamanho_maximo=40)])
    cor_fundo = factory.fuzzy.FuzzyChoice(['', Aleatorio.cor_rgb()])
    cor_texto = factory.fuzzy.FuzzyChoice(['', Aleatorio.cor_rgb()])

