from enum import Enum


class EnumFormatoDeInscricaoImobiliariaMunicipal(Enum):
    SEIS_DIGITOS_SEM_PONTO = r'\d{6}'                                   # 000000
    SEIS_DIGITOS_COM_PONTO = r'\d{3}\.\d{3}'                            # 000.000
    SEIS_DIGITOS_COM_TRACO_NA_QUARTA = r'\d{3}\-\d{3}'                  # 000-000
    SEIS_DIGITOS_COM_TRACO_NA_QUINTA = r'\d{4}\-\d{2}'                  # 0000-00
    QUINZE_DIGITOS_SEM_PONTO = r'\d{15}'                                # 000000000000000
    QUINZE_DIGITOS_COM_PONTOS = r'\d{2}\.\d{2}\.\d{3}\.\d{5}\.\d{3}'    # 00.00.00000.000
