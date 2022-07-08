import factory.fuzzy

from src.dominio.glossarios import Glossario
from src.dominio.objetos_de_valor import InscricaoImobiliariaMunicipalDeMatricula
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteInscricaoImobiliariaMunicipalDeMatricula(factory.Factory):
    class Meta:
        model = InscricaoImobiliariaMunicipalDeMatricula

    valor = factory.fuzzy.FuzzyChoice(
        InscricaoImobiliariaMunicipalDeMatricula.extrair_opcoes_compartilhadas() +
        [StringAleatoria.substituindo_caracter_por_digito(base=exemplo, substituir='0') for exemplo in Glossario.inscricao_imobiliaria_municipal.values()]
    )
