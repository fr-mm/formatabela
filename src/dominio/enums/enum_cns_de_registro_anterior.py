from enum import Enum

from src.dominio.enums import EnumOpcoesCompartilhadas


class EnumCNSDeRegistroAnterior(Enum):
    SALVADOR = '00.839-1'
    SIMOES_FILHO = '00.785-6'
    CANDEIAS = '13.960-0'
    AUSENTE = EnumOpcoesCompartilhadas.AUSENTE.value
