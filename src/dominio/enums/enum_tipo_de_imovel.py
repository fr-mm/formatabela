from enum import Enum

from src.dominio.enums.enum_opcoes_compartilhadas import EnumOpcoesCompartilhadas


class EnumTipoDeImovel(Enum):
    URBANO = 'urbano'
    RURAL = 'rural'
    AUSENTE = EnumOpcoesCompartilhadas.NAO_SE_APLICA.value
