from dataclasses import dataclass

from src.dominio.enums import EnumFormatoInscricaoImobiliariaMunicipalDeMatricula


@dataclass(init=False)
class Glossario:
    inscricao_imobiliaria_municipal = {
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.SEIS_DIGITOS_SEM_PONTO: '000000',
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.SEIS_DIGITOS_COM_PONTO: '000.000',
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.SEIS_DIGITOS_COM_TRACO_NA_QUARTA: '000-000',
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.SEIS_DIGITOS_COM_TRACO_NA_QUINTA: '0000-00',
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.QUINZE_DIGITOS_SEM_PONTO: '000000000000000',
        EnumFormatoInscricaoImobiliariaMunicipalDeMatricula.QUINZE_DIGITOS_COM_PONTOS: '00.00.000.00000.000'
    }
    exemplos_de_livro_de_registro_anterior = [
        'Livro 0',
        'Livro 0A',
        'Livro 0AA',
    ]
    exemplos_de_numero_de_ordem_de_livro_de_registro_anterior = [
        'n° 0',
        'n° 00',
        'n° 000',
        'n° 0.000',
        'n° 00.000',
        'n° 000.000',
    ]
