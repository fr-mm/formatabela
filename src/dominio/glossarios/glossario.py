from dataclasses import dataclass

from src.dominio.enums import EnumFormatoDeInscricaoImobiliariaMunicipal


@dataclass(init=False)
class Glossario:
    inscricao_imobiliaria_municipal = {
        EnumFormatoDeInscricaoImobiliariaMunicipal.SEIS_DIGITOS_SEM_PONTO: '000000',
        EnumFormatoDeInscricaoImobiliariaMunicipal.SEIS_DIGITOS_COM_PONTO: '000.000',
        EnumFormatoDeInscricaoImobiliariaMunicipal.SEIS_DIGITOS_COM_TRACO_NA_QUARTA: '000-000',
        EnumFormatoDeInscricaoImobiliariaMunicipal.SEIS_DIGITOS_COM_TRACO_NA_QUINTA: '0000-00',
        EnumFormatoDeInscricaoImobiliariaMunicipal.QUINZE_DIGITOS_SEM_PONTO: '000000000000000',
        EnumFormatoDeInscricaoImobiliariaMunicipal.QUINZE_DIGITOS_COM_PONTOS: '00.00.000.00000.000'
    }
