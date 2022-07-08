from enum import Enum

from src.dominio.matricula.enums.enum_opcoes_compartilhadas import EnumOpcoesCompartilhadas


class EnumMedidaDaArea(Enum):
    METROS_QUADRADOS = 'm2'
    HECTARES = 'ha'
    TAREFAS = 'tar'
    AUSENTE = EnumOpcoesCompartilhadas.AUSENTE.value
