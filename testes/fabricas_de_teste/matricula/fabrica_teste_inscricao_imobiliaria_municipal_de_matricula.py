import factory.fuzzy

from src.dominio.matricula.enums import EnumOpcoesCompartilhadas
from src.dominio.matricula.glossarios import Glossario
from src.dominio.matricula.objetos_de_valor import InscricaoImobiliariaMunicipalDeMatricula
from testes.fabricas_de_teste.string_aleatoria import StringAleatoria


class FabricaTesteInscricaoImobiliariaMunicipalDeMatricula(factory.Factory):
    class Meta:
        model = InscricaoImobiliariaMunicipalDeMatricula

    valor = factory.fuzzy.FuzzyChoice(
        [EnumOpcoesCompartilhadas.AUSENTE.value, EnumOpcoesCompartilhadas.NAO_SE_APLICA.value] +
        [StringAleatoria.randomizar_caracteres(base=exemplo) for exemplo in Glossario.inscricao_imobiliaria_municipal.values()]

    )
